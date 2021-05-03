from rest_framework import serializers

from .models import Producto

class ProductoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Producto
        fields = ('nombre','descripcion','precio','existencia')