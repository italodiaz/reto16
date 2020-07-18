from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    STATUS = (
        (0, 'Inactivo'),
        (1, 'Activo')
    )

    id = models.AutoField(primary_key=True)
    image_post = models.ImageField(upload_to='images/posts', max_length=255, blank=True, null=True)
    content = models.TextField()
    pub_date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.IntegerField(default=1, choices=STATUS)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.content


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField()

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return f'{self.post.content} - {self.user.username}'

class Follower(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="users")
    follower = models.ForeignKey(User, on_delete=models.CASCADE,related_name="followers")

    class Meta:
        verbose_name = 'Follower'
        verbose_name_plural = 'Followers'

    def __str__(self):
        return self.user_follower.username
