from dragonpy import Ticker


def test_is_fund():
    assert Ticker.is_fund("BPIEF5")
    assert not Ticker.is_fund("TEL")


def test_date_converter():
    dates = Ticker._time_string_to_datetime_range("ALL")
    assert dates[0].second == 0
