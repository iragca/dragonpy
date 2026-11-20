from unittest.mock import Mock

from pytest import fixture, raises

from dragonpy.services import ClientsService


@fixture
def cs():
    client = Mock()
    client.base_url = "https://devtest.dragonfi.ph"
    return ClientsService(client)


def test_verify_totp(cs: ClientsService):
    response = {"username": "dev@mail.com", "token": "token"}
    cs._post = Mock(return_value=response)

    result = cs.verify_totp("dev@mail.com", "123456")

    cs._post.assert_called_once_with(
        "VerifyTotp",
        {"username": "dev@mail.com", "key": "123456"},
    )
    assert result == response


def test_totp_6_digits(cs: ClientsService):

    with raises(ValueError, match="six"):
        cs.verify_totp("dev@mail.com", "31212")

    with raises(ValueError, match="only be digits"):
        cs.verify_totp("dev@mail.com", "abc312")


def test_verify_totp_path():
    client = Mock()
    client.base_url = "https://devtest.dragonfi.ph/api/v2/"

    service = ClientsService(client)

    assert service.service_url == "https://devtest.dragonfi.ph/api/v2/Clients"
