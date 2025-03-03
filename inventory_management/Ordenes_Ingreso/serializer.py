from rest_framework import serializers
from .models import Ordenes_Ingreso, Ordenes_Ingreso_Detalle


class Ordenes_IngresoSerializer(serializers.ModelSerializer):
    IOrden_ID = serializers.CharField(read_only=True)
    #Empleado_ID = serializers.PrimaryKeyRelatedField(source="user.id", read_only=True)
    #Proveedor_ID = serializers.PrimaryKeyRelatedField(queryset=Proveedores.objects.all())
    #Empleado_ID = serializers.PrimaryKeyRelatedField(queryset=Empleado.objects.all())

    class Meta:
        model = Ordenes_Ingreso
        fields = '__all__'

class Ordenes_Ingreso_DetalleSerializer(serializers.ModelSerializer):
    iOrdenDetalle_ID = serializers.CharField(read_only=True)
    ordenIngreso = Ordenes_IngresoSerializer()
    class Meta:
        model = Ordenes_Ingreso_Detalle
        fields = '__all__'


    def create(self, validated_data):
        #Extraer datos de la orden
        ordenes_ingreso_data = validated_data.pop('ordenIngreso')
        proveedor_id = ordenes_ingreso_data['Proveedor_ID'].id
        empleado_id = ordenes_ingreso_data['Empleado_ID'].id
        
        #Crear orden de ingreso
        orden_ingreso_serializer = Ordenes_IngresoSerializer(data={
                'fec_orden': ordenes_ingreso_data['fec_orden'], 
                'Proveedor_ID': proveedor_id, 
                'Empleado_ID': empleado_id})
        orden_ingreso_serializer.is_valid(raise_exception=True)
        orden_ingreso = orden_ingreso_serializer.save() #Guarda la orden de ingreso
        
        if isinstance(orden_ingreso, Ordenes_Ingreso):
            validated_data['IOrden_ID'] = orden_ingreso  #Asigna la instacia, no el ID
        else:
            raise TypeError("orden_ingreso no es una instancia válida de Ordenes_Ingreso")

        orden_ingreso_detalle = Ordenes_Ingreso_Detalle.objects.create(**validated_data)
        
        return orden_ingreso_detalle

        
