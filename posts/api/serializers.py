from rest_framework import serializers
from ..models import (
    Post
)
from base.api.serializers import UserPublicSerializer
from comments.api.serializers import CommentSerializer

POST_VALIDATE = ['like', 'dislike']

class PostSerializer(serializers.ModelSerializer):
    user = UserPublicSerializer(read_only=True)
    likes = serializers.SerializerMethodField(read_only=True)
    dislikes = serializers.SerializerMethodField(read_only=True)
    comments = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'user', 'image', 'day', 'description', 'date', 'datetime', 'is_private', 'view_count', 'likes', 'dislikes', 'comments')

    def get_likes(self, obj):
        like_count = obj.likes.count()
        return like_count
    
    def get_dislikes(self, obj):
        dislike_count = obj.dislikes.count()
        return dislike_count
    
    def get_comments(self, obj):
        qs = obj.comments.all()
        serializer = CommentSerializer(qs, many=True)
        return serializer.data


class PostActionSerializer(serializers.Serializer):
    action = serializers.CharField()
    def validate_action(self, value):
        value = value.lower().strip()
        if value not in POST_VALIDATE:
            raise serializers.ValidationError("This is not a valid action")
        return value 