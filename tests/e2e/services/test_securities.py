from pytest import fixture, raises

from dragonpy.exceptions.securities import StockNotFoundError
from dragonpy.services import SecuritiesService


@fixture
def service(client):
    return SecuritiesService(client)


class TestSecuritiesServices:
    def test_get_securities(self, service: SecuritiesService):
        data = service.get_stock_profile("TEL")
        assert isinstance(data, dict), data

    def test_fake_stock(self, service: SecuritiesService):
        with raises(StockNotFoundError):
            service.get_stock_profile("FAKESTOCK")
