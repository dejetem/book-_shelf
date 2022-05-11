from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .serializers import UserSerializer, LoginSerializer
from rest_framework.response import Response
from rest_framework import status, generics, permissions
from django.conf import settings
from django.contrib import auth
import jwt
from rest_framework.views import APIView


# Create your views here.
class RegisterView(GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        data = request.data
        username = data.get('username', '')
        password = data.get('password', '')
        user = auth.authenticate(username=username, password=password)

        if user:
            auth_token = jwt.encode(
                {'username': user.username}, settings.JWT_SECRET_KEY, algorithm="HS256")

            serializer = UserSerializer(user)

            data = {'user': serializer.data, 'token': auth_token}

            return Response(data, status=status.HTTP_200_OK)
            

            # SEND RESPONSE
        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class LogoutAPIView(GenericAPIView):
    #serializer_class = LogoutSerializer
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = ()
    """
     def delete(request, *args, **kwargs):
        request.user.auth_token.delete()
        # django_logout(request)
        request.user.auth_token.delete()
        return Response(status=204)
    """
    def get(self, request, format=None):
        
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)