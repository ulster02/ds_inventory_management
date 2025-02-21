from django.shortcuts import render
from rest_framework import viewsets
from .models import Clientes
from .serializer import ClientesSerializer

# Create your views here.
class ClientesViewSet(viewsets.ModelViewSet):
    queryset = Clientes.objects.all()
    serializer_class = ClientesSerializer