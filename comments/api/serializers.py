from rest_framework import serializers
from ..models import Comment
from base.api.serializers import UserPublicSerializer

class ChildCommentSeriailzer(serializers.ModelSerializer):
    user = UserPublicSerializer()
    # is_user = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'user', 'content', 'date', 'datetime')

    # def get_is_user(self, obj):
    #     request = self.context.get("request")
    #     is_user = False
    #     if request.user == obj.user:
    #         is_user = True
    #     return is_user



class CommentSerializer(serializers.ModelSerializer):
    user = UserPublicSerializer(read_only=True)
    children = serializers.SerializerMethodField(read_only=True)
    # is_user = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'user', 'content', 'date', 'datetime', 'children')

    def get_children(self, obj):
        qs = Comment.objects.filter(parent__pk=obj.pk).order_by("datetime")
        serializer = ChildCommentSeriailzer(
            qs, many=True)
        return serializer.data

    # def get_is_user(self, obj):
    #     request = self.context.get("request")
    #     is_user = False
    #     if request.user == obj.user:
    #         is_user = True
    #     return is_user