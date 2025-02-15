from rest_framework import serializers
from .models import Provincias

class ProvinciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provincias
        fields = '__all__'