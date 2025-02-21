from rest_framework import serializers
from .models import Ordenes_Egreso, EOrdenes_Detalle

class Ordenes_EgresoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ordenes_Egreso
        fields = '__all__'

class EOrdenes_DetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = EOrdenes_Detalle
        fields = '__all__'