from httpx import Client

from dragonpy.enums import DragonFiAPI
from dragonpy.services import DashboardService, FundsService, SecuritiesService


class DragonPy:
    """
    Wrapper class that includes all services needed to interface with
    the DragonFi API.

    Attributes
    ----------
    api : str
        The base URL of the DragonFi API.
        See `dragonpy.enums.api.DragonFiAPI`.
    dashboard : DashboardService
        Contains all functions under the /Dashboard route in the
        DragonFi REST API.
    funds : FundsService
        Contains all Funds related functions under the /Funds route
        in the DragonFi REST API.
    securities : SecuritiesService
        Contains all Stocks related functions under the /Securities
        route in the DragonFi REST API.
    """

    def __init__(self, url: str | DragonFiAPI = DragonFiAPI.REST_V2):
        """Instantiate the DragonPy class.

        Parameters
        ----------
        url : str
            The base URL of the DragonFi API.
            See `dragonpy.enums.api.DragonFiAPI`.
        """
        self.api = url
        self._client = Client(base_url=url, headers={"UserAgent": "dragonpy"})
        self.dashboard = DashboardService(self._client)
        self.funds = FundsService(
            self._client,
        )
        self.securities = SecuritiesService(self._client)
