from .models import Clientes
from provincias.models import Provincias
from numero.models import Numero
from rest_framework import serializers


class NumeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Numero
        fields = 'number', 'num_cod_pais'

class ClientesSerializer(serializers.Serializer):
    numero = NumeroSerializer()
    nom_cliente = serializers.CharField(max_length=65)
    apellidos_cliente = serializers.CharField(max_length=250)
    direccion = serializers.CharField(required=False, max_length=450)
    fec_nacimiento = serializers.DateField()
    #Provincia object
    provincia_cliente = serializers.PrimaryKeyRelatedField(queryset=Provincias.objects.all())
    correo_electronico = serializers.EmailField()
    
    #Modifying the create method to include the Numero object and compare it with the JSONField 
    #and be able to create in Number table
    def create(self, validated_data):
        numero_data = validated_data.pop('numero')
        cliente = Clientes.objects.create(**validated_data)

        numero_serilizer = NumeroSerializer(data=numero_data)
        numero_serilizer.is_valid(raise_exception=True)

        num_obj, created = Numero.objects.get_or_create(
            number=numero_data.get('number'),
            num_cod_pais=numero_data.get('num_cod_pais'),
            defaults=numero_serilizer.validated_data)
        cliente.num_cliente.add(num_obj)
        return cliente

        