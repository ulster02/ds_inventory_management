from rest_framework import serializers
from .models import Empleado, Rol_Empleado

class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = '__all__'

class EmpleadoRolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol_Empleado
        fields = '__all__'