from django.shortcuts import render
from rest_framework import APIView
from rest_framework.response import Response    
from rest_framework import status
from django.contrib.auth.models import User
from .models import Event 





class RegisterView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')

        if not username or not password:
            return Response({'error': 'Username and password are required'}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=username).exists():
            return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create(
            username=username,
            password=make_password(password),
            email=email
        )
        return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
    
    

