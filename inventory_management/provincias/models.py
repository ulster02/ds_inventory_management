from django.db import models

# Create your models here.
class Provincias(models.Model):
    nom_provincia = models.CharField(max_length=65)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.nom_provincia