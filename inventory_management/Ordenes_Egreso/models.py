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
    
class EOrdenes_Detalle(models.Model):
    eOrdenDetalle_ID = models.CharField(max_length=10, primary_key=True)
    cantidad = models.IntegerField(validators=[ MinValueValidator(1), MaxValueValidator(99)] , null=False)
    descuento = models.DecimalField(max_digits= 8,decimal_places=2)
    eOrden_ID = models.ForeignKey(Ordenes_Egreso,null=True, on_delete=models.SET_NULL)
    producto_ID = models.ForeignKey(Productos, null=True, on_delete=models.SET_NULL)
 
    def __str__(self):
        return self.eOrdenDetalle_ID