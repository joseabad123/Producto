# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets

from .serializers import ProductoSerializer
from .models import Producto

from django.shortcuts import render

# Create your views here.

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all().order_by('nombre')
    serializer_class = ProductoSerializer