from django.urls import path
from .views import (
    NEWESTPOSTSVIEW
)

urlpatterns = [
    path('', NEWESTPOSTSVIEW, name="all-posts")
]
