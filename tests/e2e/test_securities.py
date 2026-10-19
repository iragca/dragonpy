from dragonpy.enums import DragonFiAPI
from dragonpy.services import SecuritiesService


class TestSecuritiesServices:
    def test_get_securities(self):

        secs = SecuritiesService(DragonFiAPI.REST_V2)

        data = secs.get_stock_profile("TEL")

        assert isinstance(data, dict), data
