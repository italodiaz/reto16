from django.urls import path
from .views import PostView, CategoryView, PostSearchView

urlpatterns = [
    path('<str:category__name>/<slug:slug>', PostView.as_view(), name='post-detail'),
    path('<str:name>', CategoryView.as_view(), name='category-detail'),
    path('search/', PostSearchView.as_view(), name='search-post')
]