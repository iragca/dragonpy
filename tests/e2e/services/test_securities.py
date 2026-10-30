from httpx import Client
from pytest import fixture

from dragonpy.enums import DragonFiAPI
from dragonpy.services import SecuritiesService


@fixture
def client():
    return Client(base_url=DragonFiAPI.REST_V2)


@fixture
def service(client):
    return SecuritiesService(client)


class TestSecuritiesServices:
    def test_get_securities(self, service: SecuritiesService):
        data = service.get_stock_profile("TEL")
        assert isinstance(data, dict), data

    def test_fake_stock(self, service: SecuritiesService):
        data = service.get_stock_profile("FAKESTOCK")
        assert data == {}
