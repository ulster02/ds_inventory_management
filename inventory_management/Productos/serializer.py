from rest_framework import serializers
from .models import PMarca, Productos

class ProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productos
        fields = '__all__'

class PMarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PMarca
        fields = '__all__'