from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    STATUS = (
        (0, 'Inactivo'),
        (1, 'Activo')
    )

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    status = models.IntegerField(default=1, choices=STATUS)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['id']

    def __str__(self):
        return self.name

class Post(models.Model):
    STATUS = (
        (0, 'Inactivo'),
        (1, 'Activo')
    )

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    thumbnail = models.ImageField(upload_to='images/posts/thumbnails', max_length=255, blank=True, null=True)
    image_post = models.ImageField(upload_to='images/posts', max_length=255, blank=True, null=True)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    pub_date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.IntegerField(default=1, choices=STATUS)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['title']

    def __str__(self):
        return self.title

class Comment(models.Model):
    STATUS = (
        (0, 'Inactivo'),
        (1, 'Activo')
    )

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField()
    status = models.IntegerField(default=1, choices=STATUS)

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return f'{self.post.title} - {self.user.username}'
