from django.db import models

# Create your models here.
class Empleado(models.Model):
    nom_empleado = models.CharField(null=False, max_length=65)
    apellidos_empleado = models.CharField(null=False, max_length=250)
    fec_nacimiento = models.DateField(null=False)

    def __str__(self):
        return self.nom_empleado
    
class Rol_Empleado(models.Model):
    nom_rol_empleado = models.CharField(null=False, max_length=65)
    detalle_rol = models.TextField(max_length=250, null=True)
    empleado_ID_FK = models.ForeignKey(Empleado)

    def __str__(self):
        return self.nom_rol_empleado