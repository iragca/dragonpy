from dragonpy.enums import DragonFiEndpoint
from dragonpy.services import FundsService, SecuritiesService


class DragonPy:
    def __init__(
        self, endpoint: str | DragonFiEndpoint = DragonFiEndpoint.REST_V2
    ):
        self.endpoint = endpoint
        self.securities = SecuritiesService(endpoint)
        self.funds = FundsService(endpoint)
