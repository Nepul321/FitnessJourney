from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
    path('api/', include('base.api.urls')),
    path('api/posts/', include('posts.api.urls')),
    path('api/users/', include('users.api.urls')),
    path('api/comments/', include('comments.api.urls')),
]
