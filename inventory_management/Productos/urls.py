from django.urls import path, include
from Productos import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('pmarca', views.PMarcaViewSet, 'pmarca')
router.register('productos', views.ProductosViewSet, 'productos')

urlpatterns = [
    path('api/v1/', include(router.urls))
]