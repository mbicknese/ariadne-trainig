import os
from ariadne import ObjectType, load_schema_from_path

type_defs = load_schema_from_path(os.path.dirname(__file__) + "/schema.graphql")
query = ObjectType("Query")
client = ObjectType("Client")
resolvers = [query, client]


@query.field("config")
@client.field("config")
def resolve_config(parent, *_, id: str=None):
    return {
        "id": id or parent["config"]["id"],
        "version": "v1",
        "client": { "id": "foo" }
    }

