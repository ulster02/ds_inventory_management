from django.contrib import admin
from .models import Empleado, Rol_Empleado
# Register your models here.
admin.site.register(Empleado)
admin.site.register(Rol_Empleado)