from rest_framework import viewsets
from .models import PMarca, Productos
from .serializer import PMarcaSerializer, ProductosSerializer

# Create your views here.
class PMarcaViewSet(viewsets.ModelViewSet):
    queryset = PMarca.objects.all()
    serializer_class = PMarcaSerializer

class ProductosViewSet(viewsets.ModelViewSet):
    queryset = Productos.objects.all()
    serializer_class = ProductosSerializer
