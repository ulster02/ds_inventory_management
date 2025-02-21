from django.shortcuts import render
from rest_framework import viewsets
from .serializer import Producto_CategoriasSerializer
from .models import Producto_Categorias

# Create your views here.
class Producto_CategoriasViewSet(viewsets.ModelViewSet):
    queryset = Producto_Categorias.objects.all()
    serializer_class = Producto_CategoriasSerializer