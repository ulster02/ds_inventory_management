from django.db import models
from clientes.models import Clientes
from Empleados.models import Empleado
from Productos.models import Productos

# Create your models here.
class Ordenes_Egreso(models.Model):
    EOrden_ID = models.CharField(max_length=10, primary_key=True)
    fec_orden = models.DateTimeField(null=False)
    cliente_ID = models.ForeignKey(Clientes, null=False)
    detalle_orden = models.TextField(max_length=100)
    empleado_ID = models.ForeignKey(Empleado, null=False, on_delete=models.SET_NULL )

    def __str__(self):
        return self.EOrden_ID
    
class EOrdenes_Detalle(models.Model):
    eOrdenDetalle_ID = models.CharField(max_length=10, primary_key=True)
    cantidad = models.IntegerField(max_digits=2, null=False)
    descuento = models.DecimalField(decimal_places=2)
    eOrden_ID = models.ForeignKey(Ordenes_Egreso,null=False, on_delete=models.SET_NULL)
    producto_ID = models.ForeignKey(Productos)
    
    def __str__(self):
        return self.eOrdenDetalle_ID