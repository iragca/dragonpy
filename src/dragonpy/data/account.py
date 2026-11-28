from pydantic import BaseModel

from dragonpy.enums.dragonfi import PlanType


class Stock(BaseModel):
    symbol: str
    average_price: float
    quantity: float
    rate: float
    market_value: float
    gross_amount: float
    pct_gain_loss: float


class Fund(BaseModel):
    code: str
    name: str
    id: int
    unit: float
    average_price: float
    gross_amount: float
    market_value: float
    current_navpu: float


class Account(BaseModel):
    id: int
    account_code: str
    alias: str
    plan: PlanType
    equity: float
