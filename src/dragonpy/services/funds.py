from typing import Literal, cast

from httpx import Client

from dragonpy.enums import HTTPStatus
from dragonpy.exceptions import HTTPException
from dragonpy.exceptions.funds import FundNotFoundError
from dragonpy.responses.funds import Fund, GetFund, GetFundNAVPU

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

        Raises
        ------
        FundNotFoundError
        """
        params = {"fundCode": fundCode, "accountCode": ""}
        if accountCode is not None:
            params["accountCode"] = accountCode
        try:
            return cast(
                GetFund,
                self._get("GetFund", params),
            )
        except HTTPException as exc:
            match exc.status_code:
                case HTTPStatus.INTERNAL_SERVER_ERROR:
                    raise FundNotFoundError(fund_code=fundCode)
                case _:
                    raise

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

        Raises
        ------
        FundNotFoundError
        """

        try:
            return cast(
                GetFundNAVPU,
                self._get(
                    "GetFundNAVPU",
                    params={"fundCode": fundCode, "dateRange": dateRange},
                ),
            )
        except HTTPException as exc:
            match exc.status_code:
                case HTTPStatus.NOT_FOUND:
                    raise FundNotFoundError(fund_code=fundCode)
                case _:
                    raise

    def get_related_funds(self, fundCode: str, limit: int = 3) -> list[Fund]:
        """
        Fetch similar funds based on some unknown criteria.

        Parameters
        ----------
        fundCode : str
            The ticker symbol for the fund to search similar funds for.
        limit : int
            The nonnegative count limit of similar funds to fetch.

        Returns
        -------
        list[Fund]
            The list of similar funds.

        Raises
        ------
        FundNotFoundError
        """
        if limit < 0:
            raise ValueError(f"Limit should be nonnegative. Got {limit}.")

        try:
            data = cast(
                list,
                self._get(
                    "GetRelatedFunds", {"fundCode": fundCode, "limit": limit}
                ),
            )
            return [cast(Fund, f) for f in data]
        except HTTPException as exc:
            match exc.status_code:
                case HTTPStatus.NOT_FOUND:
                    raise FundNotFoundError(fund_code=fundCode)
                case _:
                    raise