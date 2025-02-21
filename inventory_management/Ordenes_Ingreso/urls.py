from rest_framework import routers
from Ordenes_Ingreso import views
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'ordenes_ingreso', views.OrdenesIngresoView, 'ordenes_ingreso')
router.register(r'ordenes_ingreso_detalle', views.OrdenesIngresoDetalleView, 'ordenes_ingreso_detalle')

urlpatterns = [
    path('api/v1/', include(router.urls)),
]