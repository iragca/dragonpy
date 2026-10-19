from httpx import Client

from dragonpy.enums import DragonFiAPI
from dragonpy.services import DashboardService, FundsService, SecuritiesService


class DragonPy:
    def __init__(self, url: str | DragonFiAPI = DragonFiAPI.REST_V2):
        self.api = url
        self._client = Client(base_url=url, headers={"UserAgent": "dragonpy"})
        self.dashboard = DashboardService(self._client, url)
        self.funds = FundsService(self._client, url)
        self.securities = SecuritiesService(self._client, url)
