from django.db import models

NUMERO_CHOICES = [
    ("PE","Personal"),
    ("TR", "Trabajo"),
    ("CE", "Celular"),
    ("CA", "Casa"),
]

# Create your models here.
class Numero(models.Model):
    number = models.IntegerField(max_length=8, null=False)
    num_categoria = models.CharField(choices=NUMERO_CHOICES, max_length=3)
    num_cod_pais = models.IntegerField(max_digits=3, null=False)

    def __str__(self):
        return self.number