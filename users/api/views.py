import django
django.setup()

from rest_framework.decorators import api_view
from base.api.serializers import UserSerializer
from rest_framework.response import Response
from django.contrib.auth import get_user_model
import jwt
import datetime

User = get_user_model()

@api_view(['GET'])
def UsersView(request, *args, **kwargs):
    qs = User.objects.all()
    serializer = UserSerializer(qs, many=True)
    data = serializer.data
    return Response(data, status=200)

