from django.urls import path, include
from rest_framework import routers
from provincias import views

router = routers.DefaultRouter()
router.register(r'provincias', views.ProvinciaView,'provincias')

urlpatterns = [
    path('api/v1/', include(router.urls)),

]