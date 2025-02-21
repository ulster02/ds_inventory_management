from django.shortcuts import render
from rest_framework import viewsets
from .models import Numero
from .serializer import NumeroSerializer

# Create your views here.
class NumeroViewSet(viewsets.ModelViewSet):
    queryset = Numero.objects.all()
    serializer_class = NumeroSerializer