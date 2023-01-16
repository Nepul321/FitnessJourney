import django
django.setup()

from rest_framework.decorators import api_view
from base.api.serializers import UserSerializer
from rest_framework.response import Response
from django.contrib.auth import get_user_model
import jwt
import datetime
from base.api.decorators import (
    unauthenticated_user, login_required
)
from .serializers import (
    ChangePasswordSerializer
)

User = get_user_model()

@api_view(['GET'])
def UsersView(request, *args, **kwargs):
    qs = User.objects.all()
    serializer = UserSerializer(qs, many=True)
    data = serializer.data
    return Response(data, status=200)

@api_view(['POST'])
@unauthenticated_user
def UserLoginView(request, *args, **kwargs):
    data = request.data
    email = data['email']
    password = data['password']

    if not email:
        return Response({"detail" : "Email not entered"}, status=204)

    if not password:
        return Response({"detail" : "Password not given"}, status=204)

    qs = User.objects.filter(email=email)
    if not qs:
        return Response({"detail" : "User not found"}, status=404)

    user = qs.first()

    if user.is_active == False:
        return Response({"detail" : "User is not active"}, status=401)

    if not user.check_password(password):
        return Response({"detail" : "Wrong password"}, status=401)

    payload = {
        'id': user.id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=180),
        'iat': datetime.datetime.utcnow()
    }

    token = jwt.encode(payload, 'secret', algorithm='HS256')

    response = Response()

    response.status_code = 200

    response.data = {
        "jwt" : token
    }

    return response

@api_view(['GET', 'PUT'])
@login_required
def UserAccountView(request, *args, **kwargs):
    auth = request.headers['Authorization']
    token = auth.replace("Bearer ", "")
    payload = jwt.decode(token, 'secret', algorithms=['HS256'])

    user = User.objects.filter(id=payload['id']).first()
    if request.method == "PUT":
        serializer = UserSerializer(instance=user, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=200)

    serializer = UserSerializer(user)

    return Response(serializer.data, status=200)


@api_view(['POST'])
@login_required
def UserChangePasswordView(request, *args, **kwargs):
    auth = request.headers['Authorization']
    token = auth.replace("Bearer ", "")
    payload = jwt.decode(token, 'secret', algorithms=['HS256'])
    data = request.data
    user = User.objects.filter(id=payload['id']).first()
    context = {'user' : user}
    serializer = ChangePasswordSerializer(data=data, context=context)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    payloadnew = {
        'id': user.id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
        'iat': datetime.datetime.utcnow()
    }
    newtoken = jwt.encode(payloadnew, 'secret', algorithm='HS256')

    response = Response()


    response.status_code = 200

    response.set_cookie(key="jwt", value=newtoken, httponly=True)
    response.data = {
        "jwt" : newtoken
    }

    return response