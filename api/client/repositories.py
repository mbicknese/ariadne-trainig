from abc import ABC, abstractmethod

from .mock_data import clients
from .model import Client

class ClientNotFound(Exception):
    pass

class ClientRepositoryABC(ABC):
    @abstractmethod
    async def get_client(self, id: str) -> Client:
        raise NotImplementedError

class StaticClientRepository(ClientRepositoryABC):
    async def get_client(self, id: str) -> Client:
        values = clients.get(id, None)
        if values is None:
            raise ClientNotFound
        client = Client(id=values["id"], name=values["name"], configId=values.get("config", {}).get("id", None))
        return client
