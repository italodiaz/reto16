from rest_framework import viewsets, filters
from .serializers import FollowerSerializer, PostSerializer, CommentSerializer
from .models import Follower, Post, Comment

# Create your views here.
class FollowerView(viewsets.ModelViewSet):
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer

class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CommentView(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
