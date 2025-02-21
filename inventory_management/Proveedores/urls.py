from django.urls import path, include
from rest_framework import routers
from .views import ProveedoresViewSet
from Proveedores import views


router = routers.DefaultRouter()
router.register('proveedores', views.ProveedoresViewSet, 'proveedores')

urlpatterns = [
    path('api/v1/', include(router.urls)),
]