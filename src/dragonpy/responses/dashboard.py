from typing import TypedDict


class Event(TypedDict):
    type: str
    symbol: str
    candleType: str
    open: float
    high: float
    low: float
    volume: int
    time: str
    localtime: str
    timeinSeconds: int


class Events(TypedDict):
    events: Event
