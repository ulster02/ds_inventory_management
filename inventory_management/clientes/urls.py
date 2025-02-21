from rest_framework import routers
from clientes import views
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'clientes', views.ClientesViewSet, 'clientes')

urlpatterns = [
    path('api/v1/', include(router.urls)),
]