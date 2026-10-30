from typing import Literal, cast

from httpx import Client

from dragonpy.responses.funds import GetFund, GetFundNAVPU

from .service import Service


class FundsService(Service):
    """
    Service class for DragonFI REST API route /Fund.

    Methods
    -------
    get_stock_profile(stockCode: str) -> GetStockProfile
        Fetch stock metadata and profile information.
    """

    def __init__(self, client: Client, path: str = "Fund"):
        """Instantiate this service class.

        Parameters
        ----------
        client : httpx.Client
            The HTTP client to perform HTTP requests, connections
            and sessions.
        path : str
            The base route path for Fund functions.
        """
        super().__init__(client, path)

    def get_fund(self, fundCode: str, accountCode=None) -> GetFund:
        """Fetch fund metadata and profile information.

        Parameters
        ----------
        fundCode : str
            Ticker symbol of the security or fund to fetch data.
        accountCode : optional
            [TO BE DETERMINED]

        Returns
        -------
        GetFund
            The stock's metadata and profile information.
            A typed dictionary.
        """
        return cast(
            GetFund, {"fundCode": fundCode, "accountCode": accountCode}
        )

    def get_fund_navpu(
        self,
        fundCode: str,
        dateRange: Literal["1W", "1M", "1Y", "3Y", "5Y", "ALL"] = "1Y",
    ) -> GetFundNAVPU:
        """Get time series data for a specific fund.

        Parameters
        ----------
        symbol : str
            Ticker symbol of the fund to fetch data.
        dateRange : str, optional
            Temporal coverage of the data.
            How much time is the data worth.
            1W: 1 week
            1M: 1 month
            1Y: 1 year
            3Y: 5 years
            ALL: All available data

        Returns
        -------
        GetFundNAVPU
            Includes the time series data for the stock returned from the
            API as well as some other metadata.
        """

        return cast(
            GetFundNAVPU,
            self._get(
                "GetFundNAVPU",
                params={"fundCode": fundCode, "dateRange": dateRange},
            ),
        )
