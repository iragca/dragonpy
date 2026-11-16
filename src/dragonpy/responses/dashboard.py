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


class TradeCalendar(TypedDict):
    calendarDate: str
    isMarketOpen: bool
    isHoliday: bool
    isWeekend: bool
    openTime: str
    closeTime: str
    lunchTimeStart: str
    lunchTimeEnd: str
    calendarYear: int
    remarks: str | None
    calendarDateFormatted: str
    morningSession: str
    afterNoonSession: str
    fullSession: str
    id: int
    dateEntry: str
