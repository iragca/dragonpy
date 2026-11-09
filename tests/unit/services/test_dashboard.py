from unittest.mock import Mock

import pytest
from pytest import fixture, raises

from dragonpy.exceptions.dashboard import SymbolNotFoundError
from dragonpy.exceptions.dragonpy import UnexpectedDataError
from dragonpy.services import DashboardService


@fixture
def ds():
    client = Mock()
    client.base_url = "https://devtest.dragonfi.ph"
    return DashboardService(client)


def test_get_delayed_bars(ds: DashboardService):
    ds._get = Mock(return_value={"events": [1]})

    ds.get_delayed_bars("ABC")

    args, _kwargs = ds._get.call_args

    called_params = args[1]

    assert isinstance(called_params["fromTime"], int)
    assert isinstance(called_params["toTime"], int)

    with raises(ValueError, match="must be earlier"):
        ds.get_delayed_bars("ABC", fromTime=2, toTime=1)

    with raises(ValueError, match="must not be empty"):
        ds.get_delayed_bars("")


@pytest.mark.parametrize(
    "output", [{"eventz": [1]}, "not_a_dict", {"events": 1}]
)
def test_get_delayed_bars_unexpected(ds: DashboardService, output):
    ds._get = Mock(return_value=output)

    with raises(UnexpectedDataError):
        ds.get_delayed_bars("ABC")


def test_get_delayed_bars_fake_symbol(ds: DashboardService):
    ds._get = Mock(return_value={"events": []})

    with raises(SymbolNotFoundError):
        ds.get_delayed_bars("ABC")
