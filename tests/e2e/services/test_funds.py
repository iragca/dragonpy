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
        with raises(FundNotFoundError):
            service.get_fund("FAKEFUND")

        with raises(FundNotFoundError):
            service.get_fund_navpu("FAKEFUND")
