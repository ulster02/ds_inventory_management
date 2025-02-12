from django.db import models

# Create your models here.
class Producto_Categorias(models.Model):
    nom_categoria = models.CharField(max_length=50, null=False)
    descripcion = models.TextField(null=True)

    def __str__(self):
        return self.nom_categoria