from django.db import models
from numero.models import Numero

# Create your models here.
class Proveedores:
    nom_proveedor = models.CharField(max_length=65)
    nom_contacto = models.CharField(max_length=65, null=True)
    correo_electronico = models.EmailField()
    direccion = models.TextField(max_length=450, null=True)
    num_proveedor = models.ManyToManyField(Numero)