from datetime import datetime
from typing import Literal

from dateutil.relativedelta import relativedelta
from httpx import Client

from dragonpy.services.service import Service


class DashboardService(Service):
    def __init__(self, client: Client, path: str = "Dashboard"):
        super().__init__(client, path)

    def get_delayed_bars(
        self,
        symbol: str,
        candleType: Literal["1", "5", "15", "30", "1D", "1W", "1M"] = "1D",
        count: int = 301,
        delayInMinutes: int = 15,
        time_range: tuple[datetime, datetime] | None = None,
    ):
        """Get price action data for a specified symbol.

        Parameters
        ----------
        symbol : str
            Ticker symbol of the security or fund to fetch
        candleType : str
            1: 1 minute
            5: 5 minutes
            15: 15 minutes
            30: 30 minutes
            1D: 1 day
            1W: 1 week
            1M: 1 month
        time_range : tuple[datetime, datetime] | None
            The pair of datetimes for the time range. (startDate, endDate)
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

        return self._get("GetDelayedBars", params)
