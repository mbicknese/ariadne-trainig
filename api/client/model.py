from dataclasses import dataclass

@dataclass
class Client:
    id: str
    name: str
    configId: str = None
