from functools import cached_property
from string import digits
from typing import Literal

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

    def history(self, time_range: Literal["1W", "1M"]):
        pass

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
