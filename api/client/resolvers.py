import os
from ariadne import ObjectType, load_schema_from_path
from api.config.model import Config
from .repositories import ClientRepositoryABC, StaticClientRepository, ClientNotFound

type_defs = load_schema_from_path(os.path.dirname(__file__) + "/schema.graphql")
query = ObjectType("Query")
config = ObjectType("Config")
resolvers = [query, config]

@query.field("client")
@config.field("client")
async def resolve_client(parent: Config=None, *_, id: str=None, repository: ClientRepositoryABC=StaticClientRepository()):
    try:
        return await repository.get_client(id=id or parent.clientId)
    except ClientNotFound:
        if getattr(parent, 'clientId', None) is not None:
            raise ClientNotFound("Configs should always have a client, this probably means the data set is corrupt.")
        return None
