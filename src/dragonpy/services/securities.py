from typing import cast

from httpx import Client

from dragonpy.responses.securities import GetStockProfile

from .service import Service


class SecuritiesService(Service):
    def __init__(self, client: Client, path: str = "Securities"):
        super().__init__(client, path)

    def get_stock_profile(self, stockCode: str) -> GetStockProfile:
        return cast(
            GetStockProfile,
            self._get("GetStockProfile", {"stockCode": stockCode}),
        )
