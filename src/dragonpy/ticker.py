from string import digits
from typing import Literal

from dragonpy.enums import TickerType


class Ticker:
    def __init__(self, symbol: str, type: TickerType | None = None):
        """Instantiate the DragonPy class.

        Parameters
        ----------
        symbol : str
            The fund or stock ticker symbol.
        """
        self.symbol = symbol
        self.type = type

        if type is None:
            if self.is_fund(symbol):
                self.type = TickerType.FUND
            else:
                self.type = TickerType.STOCK

    def history(self, time_range: Literal["1W", "1M"]):
        pass

    @property
    def info(self):
        pass

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
