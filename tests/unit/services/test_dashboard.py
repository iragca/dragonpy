from datetime import datetime
from unittest.mock import Mock

from dateutil.relativedelta import relativedelta
from pytest import fixture, raises

from dragonpy.exceptions.dashboard import SymbolNotFoundError
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

    with raises(TypeError):
        ds.get_delayed_bars("ABC", time_range=(1, 1))  # ty: ignore[invalid-argument-type]

    with raises(ValueError):
        ds.get_delayed_bars(
            "ABC",
            time_range=(datetime.now(), datetime.now(), datetime.now()),  # ty: ignore[invalid-argument-type]
        )

    with raises(ValueError):
        ds.get_delayed_bars(
            "ABC",
            time_range=(
                datetime.now(),
                datetime.now() - relativedelta(years=1),
            ),
        )


def test_get_delayed_bars_fake_symbol(ds: DashboardService):
    ds._get = Mock(return_value={"events": []})

    with raises(SymbolNotFoundError):
        ds.get_delayed_bars("ABC")
