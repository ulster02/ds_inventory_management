from rest_framework import serializers
from .models import Numero

class NumeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Numero
        fields = '__all__'