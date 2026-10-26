from unittest.mock import Mock

from pytest import fixture, raises

from dragonpy.exceptions import HTTPException
from dragonpy.services import Service


@fixture
def client():
    return Mock()


@fixture
def response():
    return Mock()


def test_get_http_err():
    client = Mock()
    response = Mock()
    response.status_code = 400
    client.get = Mock(return_value=response)

    s = Service(client, "dev")

    with raises(HTTPException):
        s._get("Func", {})


def test_empty_content(client, response):
    response.status_code = 200
    response.content = b""
    client.get = Mock(return_value=response)

    s = Service(client, "dev")

    data = s._get("Func", {})
    assert data == {}
