from rest_framework import serializers
from .models import Post, Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'content', 'createAt', 'updateAt']

class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True, source='comment_set')

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'like', 'date', 'comments']
