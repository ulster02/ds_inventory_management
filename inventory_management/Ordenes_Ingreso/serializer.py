from rest_framework import serializers
from .models import Ordenes_Ingreso, Ordenes_Ingreso_Detalle

class Ordenes_IngresoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ordenes_Ingreso
        fields = '__all__'

class Ordenes_Ingreso_DetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ordenes_Ingreso_Detalle
        fields = '__all__'