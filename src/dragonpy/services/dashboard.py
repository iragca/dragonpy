from datetime import datetime
from typing import Literal

from dateutil.relativedelta import relativedelta

from dragonpy.services.service import Service


class DashboardService(Service):
    def __init__(self, base_url: str, path: str = "Dashboard"):
        super().__init__(base_url, path)

    def get_delayed_bars(
        self,
        symbol: str,
        candleType: Literal["1", "5", "15", "30", "1D", "1W", "1M"] = "1D",
        count: int = 301,
        delayInMinutes=15,
        time_range=None,
    ):
        """
        1: 1 minute
        5: 5 minutes
        15: 15 minutes
        30: 30 minutes
        1D: 1 day
        1W: 1 week
        1M: 1 month
        """
        params = {
            "symbol": symbol,
            "candleType": candleType,
            "count": count,
            "delayInMinutes": delayInMinutes,
        }

        if time_range is None:
            now = datetime.now()
            params["fromTime"] = int((now - relativedelta(years=1)).timestamp())
            params["toTime"] = int(now.timestamp())

        return self._get("GetDelayedBars", params)
