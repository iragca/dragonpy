from typing import TypedDict


class CAGR(TypedDict):
    cagR1YR: float
    cagR2YR: float
    cagR3YR: float
    cagR4YR: float
    cagR5YR: float


class GetFund(TypedDict):
    fundName: str
    fundDescription: str
    fundManager: str
    currency: str
    fundCode: str
    unitPaying: bool
    fundLogoPath: str
    fundLogoPath2: str
    bloombergTicker: str
    fundCategoryId: int
    fundCategory: str
    inceptionDate: str
    minHoldingPeriod: float | None
    earlyRedemptionCharge: float | None
    earlyRedemptionChargeString: str | None
    earlyRedemptionChargeWaivedOnLoss: bool | None
    riskClassificationId: int
    riskClassification: str
    minInvestment: float
    isPERA: bool
    additionalInvestment: float
    minSelling: float
    dealingPeriodId: int
    period: str
    precision: int
    dealingPeriodCutOffTime: str
    redemptionSettlement: str
    subscriptionSettlement: str
    eligibilityResidenceCountry: str
    eligibilityCitizenshipCountry: str
    trustFee: float
    custodyFee: float
    administrationFee: float | None
    loadFee: float | None
    website: str
    prospectus: str
    planRulesDeclarationOfTrust: str
    dragonFiCommission: float
    return1yrPercent: float
    riskRatingId: int | None
    riskRating: str | None
    returnRatingId: int | None
    returnRating: str | None
    cagr: CAGR
    isClientEligible: bool | None
    eligibilityMessage: str | None
    id: int
    dateEntry: str


class NAVPU(TypedDict):
    fundId: int
    date: str
    value: float
    id: int
    dateEntry: str


class GetFundNAVPU(TypedDict):
    currentNAVPU: float
    currentNAVPUDate: str
    currentNAVPUCHange: float
    currentNAVPUChangePercent: float
    fundNAVPUList: list[NAVPU]
