from django.db import models
from Proveedores.models import Proveedores
from Empleados.models import Empleado

# Create your models here.
class Ordenes_Ingreso(models.Model):
    IOrden_ID = models.CharField(max_length=10, primary_key=True)
    fec_orden = models.DateTimeField(null=False)
    Proveedor_ID = models.ForeignKey(Proveedores, null= True, on_delete=models.SET_NULL)
    Empleado_ID = models.ForeignKey(Empleado, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.IOrden_ID
    
class Ordenes_Ingreso_Detalle(models.Model):
    iOrdenDetalle_ID = models.CharField(max_length=10, primary_key=True)
    Producto_ID = models.ForeignKey('Productos.Productos', on_delete=models.SET_NULL, null=True)
    cantidad = models.IntegerField(null=False)
    precio = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    Orden_ID = models.ForeignKey(Ordenes_Ingreso, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.iOrdenDetalle_ID