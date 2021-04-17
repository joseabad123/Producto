from django.conf.urls import include
from rest_framework import routers
#from django.urls import path
from django.conf.urls import url
from . import views

router = routers.DefaultRouter()
router.register(r'productos', views.ProductoViewSet)

urlpatterns = [
    url('', include(router.urls)),
    url('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]