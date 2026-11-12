from datetime import datetime
from typing import Literal, cast

from httpx import Client

from dragonpy.exceptions.dashboard import SymbolNotFoundError
from dragonpy.exceptions.dragonpy import UnexpectedDataError
from dragonpy.responses.dashboard import Events
from dragonpy.services.service import Service


class DashboardService(Service):
    """
    Service class for DragonFI REST API route /Dashboard.

    Methods
    -------
    get_delayed_bars(stockCode: str) -> Events
        Get time series data for a specific stock.
    """

    def __init__(self, client: Client, path: str = "Dashboard"):
        """Instantiate this service class.

        Parameters
        ----------
        client : httpx.Client
            The HTTP client to perform HTTP requests, connections
            and sessions.
        path : str
            The base route path for Dashboard functions.
        """
        super().__init__(client, path)

    def get_delayed_bars(
        self,
        symbol: str,
        fromTime: int | None = None,
        toTime: int | None = None,
        candleType: Literal["1", "5", "15", "30", "1D", "1W", "1M"] = "1D",
        count: int = 301,
        delayInMinutes: int = 15,
    ) -> Events:
        """Get time series data for a specific stock.

        Parameters
        ----------
        symbol : str
            Ticker symbol of the security or fund to fetch data.
        fromTime: int | None, optional
            Starting temporal coverage of the data.
        toTime: int | None, optional
            Ending temporal coverage of the data.
        candleType : str
            Temporal resolution of the data. How much time a candle
            (or 'bars' in a hisogram/barplot) represent.
            1: 1 minute
            5: 5 minutes
            15: 15 minutes
            30: 30 minutes
            1D: 1 day
            1W: 1 week
            1M: 1 month
        count : int
            [TO BE DETERMINED]
        delayInMinutes : int
            [TO BE DETERMINED]

        Returns
        -------
        Events
            The time series data for the stock returned from the
            API.
        """
        if symbol == "":
            raise ValueError("Symbol must not be empty.")

        if fromTime is None and toTime is None:
            fromTime = 0
            toTime = int(datetime.now().timestamp())

        if fromTime >= toTime:  # ty: ignore[unsupported-operator]
            raise ValueError("Start date must be earlier than end date.")

        params = {
            "symbol": symbol.upper().strip(),
            "candleType": candleType,
            "count": count,
            "delayInMinutes": delayInMinutes,
            "fromTime": fromTime,
            "toTime": toTime,
        }

        data = self._get("GetDelayedBars", params)

        if (
            (not isinstance(data, dict))
            or ("events" not in data)
            or (not isinstance(data["events"], list))
        ):
            raise UnexpectedDataError

        if len(data["events"]) == 0:
            raise SymbolNotFoundError(symbol)

        return cast(Events, data)
