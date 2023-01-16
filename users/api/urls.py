from django.urls import path
from .views import (
    UsersView,
    UserLoginView
)

urlpatterns = [
    path('', UsersView, name="users"),
    path('login/', UserLoginView, name="users-login"),
]
