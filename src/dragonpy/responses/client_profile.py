from typing import Any, TypedDict


class DXPosition(TypedDict):
    positionCode: str | None
    version: int
    symbol: str
    rate: float
    fpl: float
    convRate: float
    bidOpen: float | None
    askOpen: float | None
    initialMargin: float
    maintenanceMargin: float
    marginRate: float | None
    quantity: float
    quantityNotional: float
    averagePrice: float
    marketValue: float
    logoPath: str
    percentGainLoss: float
    grossAmount: float


class DXAccountMetric(TypedDict):
    account: str
    version: int
    equity: float
    balance: float
    credit: float
    marginFree: float
    openPL: float
    totalPL: float
    initialMargin: float
    maintenanceMargin: float
    availableFunds: float
    availableBalanceForWithdrawal: float
    totalGrossAmount: float
    totalPercentGainLoss: float
    totalMarketValue: float
    totalInvestmentValue: float
    totalInvestmentGainLoss: float
    totalInvestmentPercentGainLoss: float
    openPositionsCount: int
    openOrdersCount: int
    positions: list[DXPosition]
    balances: list[Any] | None


class DXAccountMetrics(TypedDict):
    statusCode: int
    metrics: list[DXAccountMetric]
    dxSessionToken: str | None


class ClientAccount(TypedDict):
    accountStatusId: int
    accountTypeId: int
    regPersonalInfoPrimaryId: int
    regPersonalInfoSecondaryId: int | None
    clientPersonalInfoPrimaryId: int
    clientPersonalInfoSecondaryId: int | None
    clientId: int
    investmentTypeId: int
    accountCode: str
    accountAlias: str
    avatarId: int
    avatarPath: str
    avatarSelfiePath: str | None
    avatarSelfiePathUrl: str | None
    isNoITF: bool | None
    isITF: bool | None
    dateITF: str | None
    itfFullName: str | None
    itfFileName: str | None
    itfPhotoPath: str | None
    itfPhotoPathUrl: str | None
    pseId: str
    noCDId: str
    taxCode: str
    currencyCode: str
    currencyId: int
    isMarginRequested: bool
    dateMarginRequested: str
    isFunded: bool
    dateFunded: str
    isDisabled: bool
    dateDisabled: str
    isSuspended: bool
    dateSuspended: str
    isDXAccCreated: bool
    dateDXCreated: str
    isTrial: bool
    startOfTrial: str
    endOfTrial: str
    isUITF: bool
    dateUITF: str
    uitfRiskClassificationId: int
    averageDailyEquity: float | None
    fundPositionsTotalMarketValue: float
    fundPositionsTotalGrossAmount: float
    fundTotalOpenPL: float
    fundTotalOpenPLPercent: float
    dxAccounts: list[Any] | None
    dxAccountMetrics: DXAccountMetrics | None
    planTypeId: int
    planType: str
    id: int
    dateEntry: str


GetClientAccountsResponse = list[ClientAccount]
