import graphene
from graphene import ObjectType, Schema
from graphene_django import DjangoObjectType
from .models import Product


class ProductType(DjangoObjectType):
    class Meta:
        model = Product


class Query(ObjectType):
    all_products = graphene.List(ProductType)

    def resolve_all_products(self, info):
        return Product.objects.all()



schema = Schema(query=Query)

