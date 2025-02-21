from django.shortcuts import render
from rest_framework import viewsets
from .models import Ordenes_Egreso, EOrdenes_Detalle
from .serializer import Ordenes_EgresoSerializer, EOrdenes_DetalleSerializer

# Create your views here.
class Ordenes_EgresoViewSet(viewsets.ModelViewSet):
    queryset = Ordenes_Egreso.objects.all()
    serializer_class = Ordenes_EgresoSerializer

class EOrdenes_DetalleViewSet(viewsets.ModelViewSet):
    queryset = EOrdenes_Detalle.objects.all()
    serializer_class = EOrdenes_DetalleSerializer