import os
from ariadne import ObjectType, load_schema_from_path
from api.client.model import Client
from .repositories import ConfigRepositoryABC, StaticConfigRepository, ConfigNotFound

type_defs = load_schema_from_path(os.path.dirname(__file__) + "/schema.graphql")
query = ObjectType("Query")
client = ObjectType("Client")
resolvers = [query, client]


@query.field("config")
@client.field("config")
async def resolve_config(parent: Client=None, *_, id: str=None, repository: ConfigRepositoryABC=StaticConfigRepository()):
    try:
        return await repository.get_config(id or parent.configId)
    except ConfigNotFound:
        return None
