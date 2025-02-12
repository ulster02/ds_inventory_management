from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

NUMERO_CHOICES = [
    ("PE","Personal"),
    ("TR", "Trabajo"),
    ("CE", "Celular"),
    ("CA", "Casa"),
]

# Create your models here.
class Numero(models.Model):
    number = models.IntegerField(validators=[MinValueValidator(11111111),MaxValueValidator(99999999)], null=False)
    num_categoria = models.CharField(choices=NUMERO_CHOICES, max_length=3)
    num_cod_pais = models.IntegerField(
        validators = [MinValueValidator(1), MaxValueValidator(999)], 
        null=False)

    def __str__(self):
        return str(self.number)