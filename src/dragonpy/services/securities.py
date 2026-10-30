from typing import cast

from httpx import Client

from dragonpy.exceptions.securities import StockNotFoundError
from dragonpy.responses.securities import GetStockProfile

from .service import Service


class SecuritiesService(Service):
    """
    Service class for DragonFI REST API route /Securities.

    Methods
    -------
    get_stock_profile(stockCode: str) -> GetStockProfile
        Fetch stock metadata and profile information.
    """

    def __init__(self, client: Client, path: str = "Securities"):
        """Instantiate this service class.

        Parameters
        ----------
        client : httpx.Client
            The HTTP client to perform HTTP requests, connections
            and sessions.
        path : str
            The base route path for Securities functions.
        """
        super().__init__(client, path)

    def get_stock_profile(self, stockCode: str) -> GetStockProfile:
        """Fetch stock metadata and profile information.

        Parameters
        ----------
        stockCode : str
            The ticker symbol or code for a security/stock.

        Returns
        -------
        GetStockProfile
            The stock's metadata and profile information.
            A typed dictionary.
        """
        data = self._get("GetStockProfile", {"stockCode": stockCode})

        if data == {}:
            raise StockNotFoundError(stockCode)

        return cast(
            GetStockProfile,
            data,
        )
