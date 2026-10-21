from unittest.mock import Mock

from pytest import raises

from dragonpy.exceptions import HTTPException
from dragonpy.services import Service


def test_get_http_err():
    client = Mock()
    response = Mock()
    response.status_code = 400
    client.get = Mock(return_value=response)

    s = Service(client, "dev")

    with raises(HTTPException):
        s._get("Func", {})
