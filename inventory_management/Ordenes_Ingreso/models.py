from django.db import models
from Proveedores.models import Proveedores
from Empleados.models import Empleado

# Create your models here.
class Ordenes_Ingreso(models.Model):
    IOrden_ID = models.CharField(max_length=10, primary_key=True)
    fec_orden = models.DateTimeField(null=False)
    Proveedor_ID = models.ForeignKey(Proveedores, null= True, on_delete=models.SET_NULL)
    Empleado_ID = models.ForeignKey(Empleado, null=True, on_delete=models.SET_NULL)

    def save(self, *args, **kwargs):
        if not self.IOrden_ID:  # Si no tiene ID, se genera uno nuevo
            ultimo_orden = Ordenes_Ingreso.objects.filter(IOrden_ID__startswith="OI-").order_by('-IOrden_ID').first()

            if ultimo_orden:
                try:
                    ultimo_numero = int(ultimo_orden.IOrden_ID.split("-")[1])  # Extraer número
                except ValueError:
                    ultimo_numero = 0
            else:
                ultimo_numero = 0  # Si no hay registros previos, empezar desde 1

            nuevo_numero = ultimo_numero + 1
            self.IOrden_ID = f"OI-{nuevo_numero:07d}"  # Genera el nuevo ID único
        
        super().save(*args, **kwargs)  # Guarda en la base de datos

    def __str__(self):
        return self.IOrden_ID
    
class Ordenes_Ingreso_Detalle(models.Model):
    iOrdenDetalle_ID = models.CharField(max_length=11, primary_key=True)
    Producto_ID = models.ForeignKey('Productos.Productos', on_delete=models.SET_NULL, null=True)
    cantidad = models.IntegerField(null=False)
    precio = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    IOrden_ID = models.OneToOneField(Ordenes_Ingreso, on_delete=models.SET_NULL, null=True)
    #Ordenes_IngresoFields = models.JSONField(db_column=None, null=True, blank=True)
    ordenIngreso = models.JSONField(db_column=None, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.iOrdenDetalle_ID:
            last_entry = Ordenes_Ingreso_Detalle.objects.order_by('-iOrdenDetalle_ID').first()
            next_entry = int(last_entry.iOrdenDetalle_ID.split('-')[-1]) +1 if last_entry else 1
            self.iOrdenDetalle_ID  = f'OID-{next_entry:06d}'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.iOrdenDetalle_ID