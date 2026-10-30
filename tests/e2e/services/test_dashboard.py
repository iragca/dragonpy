from httpx import Client
from pytest import raises

from dragonpy.exceptions.dashboard import SymbolNotFoundError
from dragonpy.services import DashboardService


class TestDashboardServices:
    def test_get_delayed_bars_fake_symbol(self, client: Client):
        dbs = DashboardService(client)

        with raises(SymbolNotFoundError):
            dbs.get_delayed_bars("FAKESYMBOL")
