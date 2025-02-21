from django.shortcuts import render
from rest_framework import viewsets
from .models import Empleado, Rol_Empleado
from .serializer import EmpleadoSerializer, EmpleadoRolSerializer

# Create your views here.
class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer

class EmpleadoRolViewSet(viewsets.ModelViewSet):
    queryset = Rol_Empleado.objects.all()
    serializer_class = EmpleadoRolSerializer