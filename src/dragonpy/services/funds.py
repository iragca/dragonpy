from httpx import Client

from .service import Service


class FundsService(Service):
    def __init__(self, client: Client, path: str = "Funds"):
        super().__init__(client, path)
