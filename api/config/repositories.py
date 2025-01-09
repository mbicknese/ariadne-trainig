from abc import ABC, abstractmethod

from .mock_data import configs
from .model import Config

class ConfigNotFound(Exception):
    pass

class ConfigRepositoryABC(ABC):
    @abstractmethod
    async def get_config(self, id: str) -> Config:
        raise NotImplementedError

class StaticConfigRepository(ConfigRepositoryABC):
    async def get_config(self, id: str) -> Config:
        values = configs.get(id, None)
        if values is None:
            raise ConfigNotFound
        config = Config(id=values["id"], version=values["version"], clientId=values.get("client", {}).get("id", None))
        return config
