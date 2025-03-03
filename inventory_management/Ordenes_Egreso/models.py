from django.db import models
from clientes.models import Clientes
from Empleados.models import Empleado
from Productos.models import Productos
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Ordenes_Egreso(models.Model):
    EOrden_ID = models.CharField(max_length=10, primary_key=True)
    fec_orden = models.DateTimeField(null=False)
    cliente_ID = models.ForeignKey(Clientes, null=True, on_delete=models.SET_NULL )
    detalle_orden = models.TextField(max_length=100)
    empleado_ID = models.ForeignKey(Empleado, null=True, on_delete=models.SET_NULL )

    def __str__(self):
        return self.EOrden_ID
    
    def save(self, *args, **kwargs):
        if not self.EOrden_ID:  # Si no tiene ID, se genera uno nuevo
            ultimo_orden = Ordenes_Egreso.objects.filter(EOrden_ID__startswith="OE-").order_by('-EOrden_ID').first()

            if ultimo_orden:
                try:
                    ultimo_numero = int(ultimo_orden.EOrden_ID.split("-")[1])  # Extraer número
                except ValueError:
                    ultimo_numero = 0
            else:
                ultimo_numero = 0  # Si no hay registros previos, empezar desde 1

            nuevo_numero = ultimo_numero + 1
            self.EOrden_ID = f"OE-{nuevo_numero:07d}"  # Genera el nuevo ID único
        
        super().save(*args, **kwargs)  # Guarda en la base de datos
    
class EOrdenes_Detalle(models.Model):
    eOrdenDetalle_ID = models.CharField(max_length=10, primary_key=True)
    cantidad = models.IntegerField(validators=[ MinValueValidator(1), MaxValueValidator(99)] , null=False)
    descuento = models.DecimalField(max_digits= 8,decimal_places=2, null=True)
    eOrden_ID = models.ForeignKey(Ordenes_Egreso,null=True, on_delete=models.SET_NULL)
    producto_ID = models.ForeignKey(Productos, null=True, on_delete=models.SET_NULL)
    ordenEgreso = models.JSONField(db_column=None, null=True, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.eOrdenDetalle_ID:
            last_entry = EOrdenes_Detalle.objects.order_by('-eOrdenDetalle_ID').first()
            next_entry = int(last_entry.eOrdenDetalle_ID.split('-')[-1]) +1 if last_entry else 1
            self.eOrdenDetalle_ID  = f'OED-{next_entry:06d}'
        super().save(*args, **kwargs)

    
    def __str__(self):
        return self.eOrdenDetalle_ID