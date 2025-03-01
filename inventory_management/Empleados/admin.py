from django.contrib import admin
from .models import Empleado, Rol_Empleado
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.
admin.site.register(Empleado)
admin.site.register(Rol_Empleado)

class EmpleadoInline(admin.StackedInline):
    model = Empleado
    can_delete = False
    verbose_name_plural = 'Empleado'
class UserAdmin(BaseUserAdmin):
    inlines = (EmpleadoInline, )