from typing import cast

from dragonpy.responses.securities import GetStockProfile

from .service import Service


class SecuritiesService(Service):
    def __init__(self, base_url: str, path: str = "Securities"):
        super().__init__(base_url, path)

    def get_stock_profile(self, stockCode: str) -> GetStockProfile:
        return cast(
            GetStockProfile,
            self._get("GetStockProfile", {"stockCode": stockCode}),
        )
