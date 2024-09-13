# usuarios/api_views.py

from rest_framework import generics, status
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from .forms import RegistroForm
from rest_framework.permissions import AllowAny

# API para registro de usuarios
class RegistroAPI(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        form = RegistroForm(request.data)
        if form.is_valid():
            form.save()
            return Response({'mensaje': 'Usuario registrado correctamente'}, status=status.HTTP_201_CREATED)
        return Response({'errores': form.errors}, status=status.HTTP_400_BAD_REQUEST)


# API para login de usuarios
class LoginAPI(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({'mensaje': 'Inicio de sesión correcto'}, status=status.HTTP_200_OK)
        return Response({'error': 'Error en la autenticación'}, status=status.HTTP_400_BAD_REQUEST)

