import os
from ariadne import ObjectType, load_schema_from_path

type_defs = load_schema_from_path(os.path.dirname(__file__) + "/schema.graphql")
query = ObjectType("Query")
config = ObjectType("Config")
resolvers = [query, config]

@query.field("client")
@config.field("client")
def resolve_client(parent, *_, id: str=None):
    return {
        "id": id or parent["config"]["id"],
        "name": "<NAME>",
        "config": {
            "id": "some-config"
        }
    }
