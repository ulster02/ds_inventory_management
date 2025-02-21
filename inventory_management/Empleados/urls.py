from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'empleados', views.EmpleadoViewSet, 'empleados')
router.register(r'EmpleadoRoles', views.EmpleadoRolViewSet, 'EmpleadoRoles')
router.register(r'users', views.UserViewSet, 'users')

urlpatterns = [ 
    path('api/v1/', include(router.urls))
]