from rest_framework import routers
from django.urls import path, include
from Producto_Categorias import views

router = routers.DefaultRouter()
router.register(r'producto_categorias', views.Producto_CategoriasViewSet, 'productos_categorias')

urlpatterns = [
    path('api/v1/', include(router.urls)),
]