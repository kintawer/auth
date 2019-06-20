from django.shortcuts import render
from django.contrib.auth import login, logout
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from auth.serializers import LoginSerializer, RegisterSerializer, UserSerializer
from auth.exceptions import LogoutFailed

class LoginView(generics.GenericAPIView):
    
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        login(request, user)
        return Response(UserSerializer(user).data)
    

class LogoutView(generics.GenericAPIView):
    
    serializer_class = UserSerializer
    
    def get(self, request):
        if not request.user.is_authenticated:
            raise LogoutFailed
        
        data = self.get_serializer(request.user).data
        logout(request)        
        return Response(data=data, status=status.HTTP_200_OK)
        