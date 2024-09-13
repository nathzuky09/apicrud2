from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate
from django.contrib import messages
from .forms import RegistroForm, LoginForm

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro exitoso.')
            return redirect('login')
    else:
        form = RegistroForm()
    return render(request, 'usuarios/registro.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            messages.success(request, 'Inicio de sesión correcto.')
            return redirect('home')
        else:
            messages.error(request, 'Error en la autenticación.')
    else:
        form = LoginForm()
    return render(request, 'usuarios/login.html', {'form': form})

def home(request):
    return render(request, 'usuarios/home.html')
