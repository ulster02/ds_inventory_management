from rest_framework import routers
from numero import views
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'numero', views.NumeroViewSet, 'numero')

urlpatterns = [
    path('api/v1/', include(router.urls))
]