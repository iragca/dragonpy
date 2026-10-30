from datetime import datetime
from typing import Literal, cast

from dateutil.relativedelta import relativedelta
from httpx import Client

from dragonpy.responses.dashboard import Events
from dragonpy.services.service import Service


class DashboardService(Service):
    """
    Service class for DragonFI REST API route /Dashboard.

    Methods
    -------
    get_delayed_bars(stockCode: str) -> Events
        Get time series data for a specific fund/stock.
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
        candleType: Literal["1", "5", "15", "30", "1D", "1W", "1M"] = "1D",
        count: int = 301,
        delayInMinutes: int = 15,
        time_range: tuple[datetime, datetime] | None = None,
    ) -> Events:
        """Get time series data for a specific fund or stock.

        Parameters
        ----------
        symbol : str
            Ticker symbol of the security or fund to fetch data.
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
        time_range : tuple[datetime, datetime] | None
            The pair of datetimes for the time range.
            (startDate, endDate)

        Returns
        -------
        Events
            The time series data for the fund/stock returned from the
            API.
        """
        if symbol == "":
            raise ValueError("Symbol must not be empty.")

        params = {
            "symbol": symbol.upper().strip(),
            "candleType": candleType,
            "count": count,
            "delayInMinutes": delayInMinutes,
        }

        if time_range is None:
            now = datetime.now()
            params["fromTime"] = int(
                (now - relativedelta(years=1)).timestamp()
            )
            params["toTime"] = int(now.timestamp())
        else:
            if len(time_range) != 2:
                raise ValueError(
                    "Time range must contain a start date and an end date."
                )

            start, end = time_range

            if not isinstance(start, datetime) or not isinstance(
                end, datetime
            ):
                raise TypeError("Time range values must be datetime objects.")

            if start >= end:
                raise ValueError("Start date must be earlier than end date.")

            params["fromTime"] = int(time_range[0].timestamp())
            params["toTime"] = int(time_range[1].timestamp())

        return cast(Events, self._get("GetDelayedBars", params))
