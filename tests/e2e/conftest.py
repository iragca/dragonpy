import pytest
from httpx import Client, Limits

from dragonpy._version import __version__
from dragonpy.enums import DragonFiAPI


@pytest.fixture(scope="session")
def client():
    limits = Limits(
        max_connections=1,
        max_keepalive_connections=1,
        keepalive_expiry=None,
    )
    with Client(
        limits=limits,
        base_url=DragonFiAPI.REST_V2,
        headers={"User-Agent": f"dragonpy/{__version__} (dev)"},
    ) as client:
        yield client
