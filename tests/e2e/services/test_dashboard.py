from httpx import Client

from dragonpy.services import DashboardService


class TestDashboardServices:
    def test_get_delayed_bars_fake_symbol(self, client: Client):
        dbs = DashboardService(client)

        data = dbs.get_delayed_bars("FAKESYMBOL")

        assert isinstance(data, dict), data
        assert data == {"events": []}
