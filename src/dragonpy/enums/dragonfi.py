from enum import IntEnum


class RiskClassification(IntEnum):
    CONSERVATIVE = 1
    MODERATE = 2
    AGGRESIVE = 3


class FundCategory(IntEnum):
    MONEY_MARKET = 1
    EQUITY_FUND = 2
    BOND_FUND = 3
    MULTI_ASSET = 4
