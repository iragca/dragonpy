from dragonpy import Ticker


def test_is_fund():
    assert Ticker.is_fund("BPIEF5")
    assert not Ticker.is_fund("TEL")
