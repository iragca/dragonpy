from dragonpy.enums import DragonFiEndpoint
from dragonpy.services import DashboardService, FundsService, SecuritiesService


class DragonPy:
    def __init__(
        self, endpoint: str | DragonFiEndpoint = DragonFiEndpoint.REST_V2
    ):
        self.endpoint = endpoint
        self.dashboard = DashboardService(endpoint)
        self.funds = FundsService(endpoint)
        self.securities = SecuritiesService(endpoint)
