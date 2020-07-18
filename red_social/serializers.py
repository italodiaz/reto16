from rest_framework import serializers
from .models import Follower, Post, Comment

class FollowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follower
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Post

class CommentSerializer(serializers.ModelSerializer):
    post = PostSerializer(many=False)
    class Meta:
        model = Comment
        fields = '__all__'
