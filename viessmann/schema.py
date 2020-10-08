from graphene import ObjectType, Schema

from catalog.schema import schema


class Query(schema.Query, ObjectType):
    pass


schema = Schema(query=Query)
