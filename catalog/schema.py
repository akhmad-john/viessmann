import graphene
from graphene import ObjectType, Schema



class Query(ObjectType):
    car = graphene.String()

    def resolve_car(self, info):
        return "Chevrolet Matiz"


schema = Schema(query=Query)

