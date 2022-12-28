from rest_framework import serializers
from ..models import (
    Post
)
from base.api.serializers import UserSerializer

class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Post
        fields = ('user', 'image', 'day', 'description', 'date', 'datetime')