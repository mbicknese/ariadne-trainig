from ariadne import load_schema_from_path, make_executable_schema, QueryType
from ariadne.asgi import GraphQL
from fastapi import FastAPI

from api.client.resolvers import resolvers as client_resolvers
from api.config.resolvers import resolvers as config_resolvers

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

# Load schema from file...
root_defs = load_schema_from_path("./api/root.graphql")
client_defs = load_schema_from_path("./api/client/schema.graphql")
config_defs = load_schema_from_path("./api/config/schema.graphql")

query = QueryType()
@query.field("version")
def resolve_version(*_):
    return "v0.0.1"

# Build an executable schema
schema = make_executable_schema(
    [root_defs, client_defs, config_defs],
    *client_resolvers, *config_resolvers,
    query
)

app.mount("/graphql/", GraphQL(schema, debug=True))
