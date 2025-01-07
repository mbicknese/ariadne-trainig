from ariadne import load_schema_from_path, make_executable_schema
from ariadne.asgi import GraphQL
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


# Load schema from file...
root_defs = load_schema_from_path("./api/root.graphql")
client_defs = load_schema_from_path("./api/client/schema.graphql")
config_defs = load_schema_from_path("./api/config/schema.graphql")

# Build an executable schema
schema = make_executable_schema([root_defs, client_defs, config_defs])

app.mount("/graphql/", GraphQL(schema, debug=True))
