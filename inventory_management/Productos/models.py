from django.db import models
from Producto_Categorias.models import Producto_Categorias
from Proveedores.models import Proveedores

# Create your models here.
class PMarca(models.Model):
    nom_marca = models.CharField(max_length=65, null=False)
    descripcion = models.TextField(max_length=255, null=True)

    def __str__(self):
        return self.nom_marca
    
class Productos(models.Model):
    nom_producto = models.CharField(max_length=65,null=False)
    descripcion = models.TextField(max_length=255, null=True)
    precio = models.DecimalField(max_digits=8,decimal_places=2)
    costo = models.DecimalField(max_digits=8, decimal_places=2)
    codigo_barras = models.CharField(max_length=14)
    fec_vencimiento = models.DateField()
    pMarca_ID = models.ForeignKey(PMarca,on_delete=models.SET_NULL, null=True)
    pCategoria_ID = models.ForeignKey(Producto_Categorias, on_delete=models.SET_NULL, null=True)
    proveedor_ID = models.ForeignKey(Proveedores, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nom_producto
    


