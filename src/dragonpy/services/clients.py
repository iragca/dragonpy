from string import digits
from typing import cast

from httpx import Client

from dragonpy.responses.clients import VerifyTotpResponse
from dragonpy.services.service import Service


class ClientsService(Service):
    """
    Service class for DragonFI REST API route /Clients.
    """

    def __init__(self, client: Client, path: str = "Clients"):
        super().__init__(client, path)

    def verify_totp(self, username: str, key: str) -> VerifyTotpResponse:
        """Verify a time-based one-time password.

        Parameters
        ----------
        username : str
            The account username (email).
        key : str
            The 6-digit one-time password.

        Returns
        -------
        VerifyTotpResponse
            The verification response returned from the API.
        """
        if len(key) != 6:
            raise ValueError("TOTP key should be six (6) digits.")

        if not set(key).issubset(digits):
            raise ValueError("TOTP should only be digits.")

        payload = {
            "username": username,
            "key": key,
        }
        return cast(VerifyTotpResponse, self._post("VerifyTotp", payload))
