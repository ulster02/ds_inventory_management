from django.contrib import admin
from .models import Ordenes_Egreso, EOrdenes_Detalle

# Register your models here.
admin.site.register(Ordenes_Egreso)
admin.site.register(EOrdenes_Detalle)