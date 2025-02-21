from django.shortcuts import render
from rest_framework import viewsets
from .models import Proveedores
from .serializer import ProveedoresSerializer

# Create your views here.
class ProveedoresViewSet(viewsets.ModelViewSet):
    queryset = Proveedores.objects.all()
    serializer_class = ProveedoresSerializer