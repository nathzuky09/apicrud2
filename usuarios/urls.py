# usuarios/urls.py

from django.urls import path
from .views import registro, login, home

urlpatterns = [
    path('registro/', registro, name='registro'),
    path('login/', login, name='login'),
    path('', home, name='home'),
]
