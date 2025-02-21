from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from .models import Empleado, Rol_Empleado
from .serializer import EmpleadoSerializer, EmpleadoRolSerializer, UserSerializer

# Create your views here.
class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer

class EmpleadoRolViewSet(viewsets.ModelViewSet):
    queryset = Rol_Empleado.objects.all()
    serializer_class = EmpleadoRolSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer