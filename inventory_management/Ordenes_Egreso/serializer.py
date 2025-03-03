from rest_framework import serializers
from .models import Ordenes_Egreso, EOrdenes_Detalle

class Ordenes_EgresoSerializer(serializers.ModelSerializer):
    EOrden_ID = serializers.CharField(read_only=True)
    class Meta:
        model = Ordenes_Egreso
        fields = '__all__'

class EOrdenes_DetalleSerializer(serializers.ModelSerializer):
    eOrdenDetalle_ID = serializers.CharField(read_only=True)
    ordenEgreso = Ordenes_EgresoSerializer()
    class Meta:
        model = EOrdenes_Detalle
        fields = '__all__'

    def create(self, validated_data):
        #Extraer datos de la orden
        ordenes_egreso_data = validated_data.pop('ordenEgreso')
        cliente_id = ordenes_egreso_data['cliente_ID'].id
        empleado_id = ordenes_egreso_data['empleado_ID'].id
        
        #Crear orden de egreso
        orden_egreso_serializer = Ordenes_EgresoSerializer(data={
                'fec_orden': ordenes_egreso_data['fec_orden'], 
                'Proveedor_ID': cliente_id,
                'detalle_orden':  ordenes_egreso_data['detalle_orden'],
                'Empleado_ID': empleado_id})
        orden_egreso_serializer.is_valid(raise_exception=True)
        orden_egreso = orden_egreso_serializer.save() #Guarda la orden de ingreso
        
        if isinstance(orden_egreso, Ordenes_Egreso):
            validated_data['eOrden_ID'] = orden_egreso  #Asigna la instacia, no el ID
        else:
            raise TypeError("orden_egreso no es una instancia válida de Ordenes_Egreso")

        orden_egreso_detalle = EOrdenes_Detalle.objects.create(**validated_data)
        
        return orden_egreso_detalle