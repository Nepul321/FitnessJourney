import django
django.setup()

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import PostSerializer, PostActionSerializer
from django.contrib.auth import get_user_model
from ..models import Post, PostView
from django.db.models import Q
import jwt

User = get_user_model()


@api_view(['GET'])
def NEWESTPOSTSVIEW(request, *args, **kwargs):
    qs = Post.objects.filter(
        Q(is_private=False) 
    )
    serializer = PostSerializer(qs, many=True)
    data = serializer.data
    return Response(data, status=200)

@api_view(['GET', 'POST'])
def PostView(request, id,  *args, **kwargs):
    qs = Post.objects.filter(id=id)
    if not qs:
        return Response({"detail" : "Post not found"}, status=404)
    obj = qs.first()
    try:
        auth = request.headers['Authorization']
        token = auth.replace("Bearer ", "")
    except:
        token = None

    user = None

    try:
     if token:
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        user = User.objects.filter(id=payload['id']).first()
        view = PostView.objects.create(
            user=user
        )
        view.save()
        obj.views.add(view)
        obj.set_view_count()
    except jwt.ExpiredSignatureError:
        pass

    if obj.is_private == True:
        if obj.user != user:
            return Response({"detail" : "You can't view this post"}, status=403)
    
    obj.set_view_count()

    if request.method == "POST" and user:
        data = request.data
        serializer = PostActionSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            validated_data = serializer.validated_data
            action = validated_data.get("action")
            if action == "like":
                liked = False
                if obj.likes.filter(id=user.id).exists():
                    obj.likes.remove(user)
                    liked = False
                else:
                    obj.likes.add(user)
                    try:
                        obj.dislikes.remove(user)
                    except:
                        pass
                    liked = True
                serializer = PostActionSerializer(obj)
                data = serializer.data
                return Response(data, status=200)
            elif action == "dislike":
                disliked = False
                if obj.dislikes.filter(id=user.id).exists():
                    obj.dislikes.remove(user)
                    disliked = False
                else:
                    obj.dislikes.add(user)
                    try:
                        obj.likes.remove(user)
                    except:
                        pass
                    disliked = True
                serializer = PostActionSerializer(obj)
                data = serializer.data
                return Response(data, status=200)
            else:
                return Response({"detail" : "Action not valid"}, status=401)

    
    serializer = PostSerializer(obj)
    data = serializer.data

    return Response(data, status=200)