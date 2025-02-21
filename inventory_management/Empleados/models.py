from django.db import models

# Create your models here.
class Empleado(models.Model):
    nom_empleado = models.CharField(null=False, max_length=65)
    apellidos_empleado = models.CharField(null=False, max_length=250)
    fec_nacimiento = models.DateField(null=False)
    rol_empleado_FK = models.ForeignKey('Rol_Empleado', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.rol_empleado_FK} - {self.nom_empleado} {self.apellidos_empleado} "
    
class Rol_Empleado(models.Model):
    nom_rol_empleado = models.CharField(null=False, max_length=65)
    detalle_rol = models.TextField(max_length=250, null=True)

    def __str__(self):
        return self.nom_rol_empleado