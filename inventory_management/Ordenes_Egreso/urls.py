from rest_framework import routers
from Ordenes_Egreso import views
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'Ordenes_Egreso', views.Ordenes_EgresoViewSet, 'Ordenes_Egreso')
router.register(r'EOrdenes_Detalle', views.EOrdenes_DetalleViewSet, 'EOrdenes_Detalle')

urlpatterns = [
    path('api/v1/', include(router.urls)),
]