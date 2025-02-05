from django.db import models
from provincias.models import Provincias

# Create your models here.
class Clientes(models.Model):
    nom_cliente = models.CharField(max_length=65)
    apellidos_cliente = models.CharField(max_length=250)
    direccion = models.TextField(null=True, max_length=450)
    fec_nacimiento = models.DateField()
    #Provincia object
    provincia_cliente = models.ForeignKey(Provincias, on_delete=models.SET_NULL, null=True)
    correo_electronico = models.EmailField()

    def __str__(self):
        return self.nom_cliente