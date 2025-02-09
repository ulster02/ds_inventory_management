from django.db import models
from Proveedores.models import Proveedores
from Empleados.models import Empleado

# Create your models here.
class Ordenes_Ingreso(models.Model):
    IOrden_ID = models.CharField(max_length=10, primary_key=True)
    fec_orden = models.DateTimeField(null=False)
    Proveedor_ID = models.ForeignKey(Proveedores, null= False)
    Empleado_ID = models.ForeignKey(Empleado, null=False)

    def __str__(self):
        return self.IOrden_ID
    
class Ordenes_Ingreso_Detalle(models.Model):
    IOrdenDetalle_ID = models.ForeignKey(Ordenes_Ingreso, null=False)
    Producto_ID = models.ForeignKey('Productos.Productos', null=False)
    cantidad = models.IntegerField(null=False)
    precio = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    Orden_ID = models.ForeignKey(Ordenes_Ingreso, null=False)

    def __str__(self):
        return self.IOrden_ID