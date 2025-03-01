from django.urls import path, include, re_path
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'empleados', views.EmpleadoViewSet, 'empleados')
router.register(r'EmpleadoRoles', views.EmpleadoRolViewSet, 'EmpleadoRoles')
router.register(r'users', views.UserViewSet, 'users')

urlpatterns = [ 
    path('api/v1/', include(router.urls)),
    re_path(r'login', views.login),
    re_path(r'register', views.register),
    re_path(r'profile', views.profile),
]