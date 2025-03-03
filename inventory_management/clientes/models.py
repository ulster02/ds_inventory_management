from django.db import models
from provincias.models import Provincias
from numero.models import Numero

# Create your models here.
class Clientes(models.Model):
    nom_cliente = models.CharField(max_length=65)
    apellidos_cliente = models.CharField(max_length=250)
    direccion = models.TextField(null=True, max_length=450)
    fec_nacimiento = models.DateField()
    #Provincia object
    provincia_cliente = models.ForeignKey(Provincias, on_delete=models.SET_NULL, null=True)
    correo_electronico = models.EmailField()
    
    #JSONField to include Number and code_contry in a single form
    numero = models.JSONField(db_column=None, null=True, blank=True)
    #Many to many field - Clientes/Numero
    num_cliente = models.ManyToManyField(Numero, null=True)

    def __str__(self):
        return f"{self.nom_cliente} {self.apellidos_cliente}"