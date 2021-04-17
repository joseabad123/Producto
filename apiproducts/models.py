# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=250)
    precio = models.FloatField(max_length=10)
    existencia = models.IntegerField(max_length=10)
    
    def __str__(self):
        return self.nombre