from httpx import Client

from dragonpy.enums import DragonFiAPI
from dragonpy.services import SecuritiesService


class TestSecuritiesServices:
    def test_get_securities(self):
        client = Client(base_url=DragonFiAPI.REST_V2)

        secs = SecuritiesService(client)

        data = secs.get_stock_profile("TEL")

        assert isinstance(data, dict), data
