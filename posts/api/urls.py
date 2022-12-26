from django.urls import path
from .views import (
    ALLPOSTSVIEW
)

urlpatterns = [
    path('', ALLPOSTSVIEW, name="all-posts")
]
