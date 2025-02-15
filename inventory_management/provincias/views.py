from rest_framework import viewsets
from .serializer import ProvinciaSerializer
from .models import Provincias

# Create your views here.
class ProvinciaView(viewsets.ModelViewSet):
    queryset = Provincias.objects.all()
    serializer_class = ProvinciaSerializer