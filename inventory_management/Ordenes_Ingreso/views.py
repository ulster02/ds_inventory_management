from django.shortcuts import render
from rest_framework import viewsets
from .models import Ordenes_Ingreso, Ordenes_Ingreso_Detalle
from .serializer import Ordenes_IngresoSerializer, Ordenes_Ingreso_DetalleSerializer

# Create your views here.
class OrdenesIngresoView(viewsets.ModelViewSet):
    queryset = Ordenes_Ingreso.objects.all()
    serializer_class = Ordenes_IngresoSerializer

class OrdenesIngresoDetalleView(viewsets.ModelViewSet):
    queryset = Ordenes_Ingreso_Detalle.objects.all()
    serializer_class = Ordenes_Ingreso_DetalleSerializer