from datetime import datetime
from unittest.mock import Mock

from dateutil.relativedelta import relativedelta

from dragonpy import Ticker


def test_is_fund():
    assert Ticker.is_fund("BPIEF5")
    assert not Ticker.is_fund("TEL")


def test_date_converter_all_starts_at_epoch():
    start, end = Ticker._time_string_to_datetime_range("ALL")
    assert start == datetime.fromtimestamp(0)
    assert end >= start


def test_date_converter_ranges():
    now = datetime.now()
    cases = {
        "1W": relativedelta(weeks=1),
        "1M": relativedelta(months=1),
        "1Y": relativedelta(years=1),
        "3Y": relativedelta(years=3),
        "5Y": relativedelta(years=5),
    }
    for label, delta in cases.items():
        start, end = Ticker._time_string_to_datetime_range(label)
        assert end >= start
        # start should be approximately now - delta
        expected = now - delta
        assert abs((start - expected).total_seconds()) < 5


def test_history_stock_uses_timestamps_for_delayed_bars():
    ticker = Ticker("TEL")
    ticker.dpy.dashboard.get_delayed_bars = Mock(return_value={"events": []})

    ticker.history("1Y")

    _, kwargs = ticker.dpy.dashboard.get_delayed_bars.call_args
    assert kwargs["fromTime"] == int(kwargs["fromTime"])
    assert kwargs["toTime"] == int(kwargs["toTime"])
    assert kwargs["fromTime"] < kwargs["toTime"]
