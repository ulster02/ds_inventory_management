from django.db import models
from Producto_Categorias.models import Producto_Categorias
from Proveedores.models import Proveedores
# Create your models here.
class Productos(models.Model):
    nom_producto = models.CharField(null=False)
    descripcion = models.TextField(max_length=255, null=True)
    precio = models.DecimalField(decimal_places=2)
    costo = models.DecimalField(decimal_places=2)
    codigo_barras = models.CharField(max_length=14)
    fec_vencimiento = models.DateField()
    pMarca_ID = models.ForeignKey(models.PMarca)
    pCategoria_ID = models.ForeignKey(Producto_Categorias)
    proveedor_ID = models.ForeignKey(Proveedores)
    

class PMarca(models.Model):
    nom_marca = models.CharField(max_length=65, null=False)
    descripcion = models.TextField(max_length=255, null=True)

    def __str__(self):
        return self.nom_marca
