import graphene
from graphene_django import DjangoObjectType
from .models import *


class ProductType(DjangoObjectType):
    class Meta:
        model = Producto

class Query(graphene.ObjectType):
    products = graphene.List(ProductType)

    def resolve_products(self, info, **kwargs):
        return Producto.objects.all()