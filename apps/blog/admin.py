from django.contrib import admin
from .models import Category, Post, Comment

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'get_status']

    def get_status(self, obj):
        if obj.status == 1:
            return 'Activo'
        return 'Inactivo'

    get_status.short_description = 'status'

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug', 'pub_date', 'user']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'post', 'user']

# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)