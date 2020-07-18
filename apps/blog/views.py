from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from django.db.models import Q


from .models import Post, Category, Comment

# Create your views here.
class Home(TemplateView):
    template_name = 'blog/index.html'

    def get_context_data(self, **kwargs):
        posts = Post.objects.filter(status=1)
        categories = Category.objects.filter(status=1)
        context = super(Home, self).get_context_data(**kwargs)
        context['posts'] = posts
        context['categories'] = categories
        return context

class PostView(DetailView):
    model = Post
    template_name = 'blog/detail.html'

    def get_context_data(self, **kwargs):
        slug = self.kwargs.get('slug')
        comments = Comment.objects.filter(status=1, post__slug=slug)
        context = super().get_context_data(**kwargs)
        context['comments'] = comments
        return context

    def post(self, request, **kwargs):
        post_comment = request.POST['comment']
        post_id = request.POST['id']
        Comment.objects.create(user_id=request.user.id, post_id=post_id, comment=post_comment)
        self.get_object()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

class CategoryView(TemplateView):
    template_name = 'blog/category.html'

    def get_context_data(self, **kwargs):
        posts = Post.objects.filter(status=1, category__name=kwargs['name'])
        categories = Category.objects.filter(status=1)
        context = super(CategoryView, self).get_context_data(**kwargs)
        context['posts'] = posts
        context['categories'] = categories
        return context

class PostSearchView(TemplateView):
    template_name = 'blog/search.html'

    def post(self, request):
        post_name = request.POST['post_name']
        posts = Post.objects.filter(Q(title__contains=post_name) | Q(content__contains=post_name), status=1)
        categories = Category.objects.filter(status=1)
        context = self.get_context_data()
        context['posts'] = posts
        context['categories'] = categories
        return self.render_to_response(context=context)
