from datetime import datetime
from unittest.mock import Mock

from dateutil.relativedelta import relativedelta
from pytest import fixture, raises

from dragonpy.services import DashboardService


@fixture
def ds():
    return DashboardService("https://devtest.dragonfi.ph")


def test_get_delayed_bars(ds: DashboardService):
    ds._get = Mock()

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
