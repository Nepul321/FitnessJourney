from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import PostSerializer
from ..models import Post

@api_view(['GET'])
def ALLPOSTSVIEW(request, *args, **kwargs):
    qs = Post.objects.all()
    serializer = PostSerializer(qs, many=True)
    data = serializer.data
    return Response(data, status=200)