from pydantic import BaseModel

from dragonpy.enums.dragonfi import PlanType


class Account(BaseModel):
    id: int
    account_code: str
    alias: str
    plan: PlanType
    equity: float
