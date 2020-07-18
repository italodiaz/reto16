from django.urls import path, include
from rest_framework import routers
from .views import FollowerView, PostView, CommentView

router = routers.DefaultRouter()
router.register('follower', FollowerView)
router.register('post', PostView, basename='post')
router.register('comment', CommentView)

urlpatterns = [
    path('', include(router.urls))
]