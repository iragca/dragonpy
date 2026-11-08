from typing import Literal, cast

from httpx import Client

from dragonpy.enums import HTTPStatus
from dragonpy.exceptions import HTTPException
from dragonpy.exceptions.funds import FundNotFoundError
from dragonpy.responses.funds import (
    Fund,
    FundCategory,
    FundRiskClassification,
    GetFund,
    GetFundNAVPU,
    GetFundPagedList,
)

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

    def get_fund_paged_list(
        self,
        FilterValue: str | None = None,
        Asc: bool = False,
        FilterBy: Literal[
            "fundCode", "fundName", "fundManager", "bloombergTicker"
        ] = "fundName",
        SortBy: Literal[
            "return1yr",
            "return1yrPercent",
            "return3yr",
            "return3yrPercent",
            "currentNAVPU",
        ] = "return1yrPercent",
        PageNum: int = 1,
        PageSize: int = 10,
        fundCategory: Literal[
            "Equity Fund", "Bond Fund", "Money Markey", "Multi-Asset"
        ]
        | None = None,
        RiskClassification: Literal[1, 2, 3] | None = None,
        isPera: bool | None = None,
    ) -> GetFundPagedList:
        """Search for funds.
        Fetch a filtered, sorted and paginated list of funds.
        Filtering seems to be based on similarity.

        Parameters
        ----------
        FilterValue : str | None, optional
            The value to filter funds by. Matched against ``FilterBy``.
            Defaults to None.
        Asc : bool, optional
            Whether to sort in ascending order. Defaults to False.
        FilterBy : Literal[
                    "fundCode",
                    "fundName",
                    "fundManager",
                    "bloombergTicker"
                   ], optional
            The fund field to filter on. Defaults to ``fundName``.
        SortBy : Literal[
                    "return1yr",
                    "return1yrPercent",
                    "return3yr",
                    "return3yrPercent",
                    "currentNAVPU"
                 ], optional
            The fund field to sort on. Defaults to ``return1yrPercent``.
        PageNum : int, optional
            The page number to fetch. Defaults to 1.
        PageSize : int, optional
            The number of funds per page. Defaults to 10.
        fundCategory : Literal[
                        "Equity Fund",
                        "Bond Fund",
                        "Money Market",
                        "Multi-Asset"
                       ] | None, optional
            The fund category name to filter funds by. Default to None.
        RiskClassification : Literal[1, 2, 3] | None, optional
            The risk classification ID to filter funds by. Defaults to
            None.
        isPera : bool | None, optional
            Whether to filter for PERA funds. Defaults to None.

        Returns
        -------
        GetFundPagedList
            The page of funds and the total count of matching funds.
            A typed dictionary.
        """
        params = {
            "Asc": "true" if Asc else "false",
            "FilterBy": FilterBy,
            "SortBy": SortBy,
            "PageNum": PageNum,
            "PageSize": PageSize,
        }

        self._add_optional_params(
            params,
            FilterValue=FilterValue,
            RiskClassification=RiskClassification,
            fundCategory=fundCategory,
        )

        if isPera is not None:
            params["isPera"] = "true" if isPera else "false"

        return cast(
            GetFundPagedList,
            self._get("GetFundPagedList", params),
        )

    def get_fund_categories(self) -> list[FundCategory]:
        """Get fund categories

        Returns
        -------
        list[FundCategory]
            The list of fund categories.
        """
        return [
            cast(FundCategory, fc) for fc in self._get("GetFundCategories")
        ]

    def get_fund_risk_classifications(self) -> list[FundRiskClassification]:
        """Get fund risk classifications

        Returns
        -------
        list[FundRiskClassification]
            The list of fund risk classifications.
        """
        return [
            cast(FundRiskClassification, r)
            for r in self._get("GetFundRiskClassifications")
        ]
