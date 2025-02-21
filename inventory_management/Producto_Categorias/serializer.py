from rest_framework import serializers
from .models import Producto_Categorias

class Producto_CategoriasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto_Categorias
        fields = '__all__'