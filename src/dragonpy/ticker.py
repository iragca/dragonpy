from datetime import datetime
from functools import cached_property
from string import digits
from typing import Literal

from dateutil.relativedelta import relativedelta

from dragonpy.enums import TickerType
from dragonpy.responses.funds import GetFund
from dragonpy.responses.securities import GetStockProfile

from .wrapper import DragonPy


class Ticker:
    def __init__(
        self, symbol: str, type: TickerType | None = None, **wrapper_kwargs
    ):
        """Instantiate the DragonPy class.

        Parameters
        ----------
        symbol : str
            The fund or stock ticker symbol.
        """
        self.symbol = symbol
        self.type = type
        self.dpy = DragonPy(**wrapper_kwargs)

        if type is None:
            if self.is_fund(symbol):
                self.type = TickerType.FUND
            else:
                self.type = TickerType.STOCK

    def history(
        self, date_range: Literal["1W", "1M", "1Y", "3Y", "5Y", "ALL"] = "1Y"
    ):
        """Daily historical prices for a fund or stock"""
        if self.is_fund(self.symbol):
            return self.dpy.funds.get_fund_navpu(
                self.symbol, dateRange=date_range
            )
        else:
            start, end = self._time_string_to_datetime_range(date_range)
            return self.dpy.dashboard.get_delayed_bars(
                self.symbol,
                fromTime=int(start.timestamp()),
                toTime=int(end.timestamp()),
            )

    @staticmethod
    def _time_string_to_datetime_range(
        s: Literal["1W", "1M", "1Y", "3Y", "5Y", "ALL"],
    ) -> tuple[datetime, datetime]:
        """Convert date range string shorthands
        to datetime objects

        Parameters
        ----------
        s : Literal["1W", "1M", "1Y", "3Y", "5Y", "ALL"]
            The string shorthand to convert.

        Returns
        -------
        tuple[datetime, datetime]
            The datetime range (start_datetime, end_datetime).
        """
        unix_start = datetime.fromtimestamp(0)
        now = datetime.now()
        match s:
            case "1W":
                return (now - relativedelta(weeks=1), now)
            case "1M":
                return (now - relativedelta(months=1), now)
            case "1Y":
                return (now - relativedelta(years=1), now)
            case "3Y":
                return (now - relativedelta(years=3), now)
            case "5Y":
                return (now - relativedelta(years=5), now)
            case "ALL":
                return (unix_start, now)
            case _:
                raise ValueError(
                    'Unknown string literal. Must be one of "1W", "1M", "1Y", "3Y", "5Y", "ALL"'
                )

    @cached_property
    def info(self) -> GetFund | GetStockProfile:
        """Fund or stock metatadata.

        Returns
        -------
        GetFund | GetStockProfile
            The fund or stock metadata.
        """
        if self.is_fund(self.symbol):
            return self.dpy.funds.get_fund(self.symbol)
        else:
            return self.dpy.securities.get_stock_profile(self.symbol)

    @property
    def calendar(self):
        pass

    @staticmethod
    def is_fund(symbol: str) -> bool:
        """Determines if a ticker symbol is a fund or stock.
        Checks if there are digits in the ticker symbol as a heuristic.

        Parameters
        ----------
        symbol: str
            The ticker symbol to determine.

        Returns
        -------
        bool
            Whether the provided ticker symbol is a fund or not.
            Have numbers? -> True.
        """
        return not set(digits).isdisjoint(set(symbol))
