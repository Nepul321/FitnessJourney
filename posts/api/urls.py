from django.urls import path
from .views import (
    NEWESTPOSTSVIEW,
    PostView
)

urlpatterns = [
    path('', NEWESTPOSTSVIEW, name="all-posts"),
    path('<int:id>/', PostView, name="individual-post")
]
