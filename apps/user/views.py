from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializers
from django.shortcuts import render
from rest_framework import status
from .models import CustomUser

class RegisterView(APIView):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        serializer = UserSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User create successfully!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LogoutView(APIView):
    def get(self, request):
        logout(request)
        return render(request, 'index.html')

class LoginView(APIView):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'login.html')
        else:
            return render(request, 'login.html', {'error': 'Username yoki password is error'})

class PasswordResetView(APIView):
    def get(self, request):
        return render(request, 'password_reset_form.html')

    def post(self, request):
        username = request.data.get('username')
        new_password = request.data.get('new_password')

        try:
            user = CustomUser.objects.get(username=username)  
            user.password = make_password(new_password) 
            user.save()
            return render(request, 'login.html', {'message': 'Password changed successfully!'})
        except CustomUser.DoesNotExist:
            return render(request, 'password_reset_form.html', {'error': 'User not found'})