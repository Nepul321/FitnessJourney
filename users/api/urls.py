from django.urls import path
from .views import (
    UsersView,
    UserLoginView,
    UserAccountView
)

urlpatterns = [
    path('', UsersView, name="users"),
    path('login/', UserLoginView, name="users-login"),
    path('user/', UserAccountView, name="users-view"),
]
