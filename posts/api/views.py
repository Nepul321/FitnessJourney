from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import PostSerializer
from ..models import Post
from django.db.models import Q

@api_view(['GET'])
def NEWESTPOSTSVIEW(request, *args, **kwargs):
    qs = Post.objects.filter(
        Q(is_private=False) 
    )
    serializer = PostSerializer(qs, many=True)
    data = serializer.data
    return Response(data, status=200)