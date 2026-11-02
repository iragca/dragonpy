from pytest import fixture, raises

from dragonpy.exceptions.funds import FundNotFoundError
from dragonpy.responses.funds import GetFund
from dragonpy.services import FundsService


@fixture(scope="class")
def service(client):
    return FundsService(client)


class TestFundsServices:
    def test_get_fund(self, service: FundsService):
        data: GetFund = service.get_fund("BPIEF5")
        assert isinstance(data, dict), data
        assert "fundName" in data

    def test_fake_fund(self, service: FundsService):
        ticker = "FAKEFUND"
        with raises(FundNotFoundError):
            service.get_fund(ticker)

        with raises(FundNotFoundError):
            service.get_fund_navpu(ticker)

        with raises(FundNotFoundError):
            service.get_related_funds(ticker)

    def test_limit_positive(self, service: FundsService):
        with raises(ValueError, match="nonnegative"):
            service.get_related_funds("BPIEF5", limit=-1)
