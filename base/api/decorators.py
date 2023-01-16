import django
django.setup()

from rest_framework.response import Response
from django.contrib.auth import get_user_model
import jwt

User = get_user_model()

def login_required(view):
    def wrapper_function(request, *args, **kwargs):
        try:
            auth = request.headers['Authorization']
            token = auth.replace("Bearer ", "")
        except:
            token = None
        if not token:
           return Response({"detail" : "Unauthenticated"}, status=403)
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
            user = User.objects.filter(id=payload['id']).first()
        except jwt.ExpiredSignatureError:
            return Response({"detail" : "Unauthenticated"}, status=403)

        if not user:
            return Response({"detail" : "Unauthenticated"}, status=403)

        else:
            return view(request, *args, **kwargs)

    return wrapper_function

def unauthenticated_user(view_func):
    def wrapper_function(request, *args, **kwargs):
        try:
            auth = request.headers['Authorization']
            token = auth.replace("Bearer ", "")
        except:
            token = None
            
        user = None
        try:
            if token:
                payload = jwt.decode(token, 'secret', algorithms=['HS256'])
                user = User.objects.filter(id=payload['id']).first()
        except jwt.ExpiredSignatureError:
               pass
        
        if user:
            return Response({"detail" : "You are logged in"})
        return view_func(request, *args, **kwargs)
    return wrapper_function