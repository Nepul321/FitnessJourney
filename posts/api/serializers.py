from rest_framework import serializers
from ..models import (
    Post
)
from base.api.serializers import UserSerializer

class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    likes = serializers.SerializerMethodField(read_only=True)
    dislikes = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Post
        fields = ('user', 'image', 'day', 'description', 'date', 'datetime', 'is_private', 'view_count', 'likes', 'dislikes')

    def get_likes(self, obj):
        like_count = obj.likes.count()
        return like_count
    
    def get_dislikes(self, obj):
        dislike_count = obj.dislikes.count()
        return dislike_count

    