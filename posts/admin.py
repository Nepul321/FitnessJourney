from django.contrib import admin
from .models import Post, PostView

admin.site.register(Post)
admin.site.register(PostView)