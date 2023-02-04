import django
django.setup()

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import PostSerializer
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

@api_view(['GET'])
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
    
    serializer = PostSerializer(obj)
    data = serializer.data

    return Response(data, status=200)
