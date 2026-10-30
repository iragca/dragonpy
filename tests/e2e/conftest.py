import pytest
from httpx import Client, Limits

from dragonpy.enums import DragonFiAPI


@pytest.fixture(scope="session")
def client():
    limits = Limits(
        max_connections=1,
        max_keepalive_connections=1,
        keepalive_expiry=None,
    )
    with Client(limits=limits, base_url=DragonFiAPI.REST_V2) as client:
        yield client
