from typing import TypedDict


class RelatedStock(TypedDict):
    stockCode: str
    logoPath: str | None
    change: float
    changePercent: float
    price: float


class GetStockProfile(TypedDict):
    description: str
    symbol: str
    full_name: str
    type: str
    exchange: str
    codeAndName: str
    price: float
    prevDayClosePrice: float
    dayOpenPrice: float
    bidPrice: float | None
    askPrice: float | None
    change: float
    changePercent: float
    lastTradeTime: str
    isMarketOpen: bool
    relatedStocks: list[RelatedStock]
    dayChangePricePercent: float
    averageVolume10: float
    averageVolume20: float
    dayVolume: float
    dayLowPrice: float
    dayHighPrice: float
    weekHigh52: float
    weekLow52: float
    companyName: str
    companyShortName: str
    stockCode: str
    website: str
    logoPath: str
    productCode: str
    shariahIndicator: str
    industryId: int
    industryCode: str
    industryName: str
    sectorId: int
    sectorCode: str
    sectorName: str
    listingDate: str | None
    parValue: float
    lacp: float
    shortSellingEligible: bool
    isREIT: bool
    isPreferredStock: bool | None
    preferredParentStockCode: str | None
    isPERA: bool
    floatLevel: float
    sharesOutstanding: int
    sharesFloat: int
    isin: str
    isDDS: bool | None
    isDelisted: bool | None
    isOldSymbol: bool
    isIndices: bool
    dateDelisted: str | None
    oldStockCode: str | None
    oldCompanyName: str | None
    dividendYield: float
    id: int
