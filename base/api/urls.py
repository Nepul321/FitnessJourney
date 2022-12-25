from django.urls import path
from .views import (
    APIBASEPOINT
)

urlpatterns = [
    path('', APIBASEPOINT, name="api-base")
]
