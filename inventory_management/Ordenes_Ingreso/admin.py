from django.contrib import admin
from .models import Ordenes_Ingreso, Ordenes_Ingreso_Detalle

# Register your models here.
admin.site.register(Ordenes_Ingreso)
admin.site.register(Ordenes_Ingreso_Detalle)