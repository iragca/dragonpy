import base64
import json
from typing import cast

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from httpx import Client

from dragonpy.responses.authorization import LoginResponse
from dragonpy.services.service import Service


class AuthorizationService(Service):
    """
    Service class for DragonFI REST API route /Authorization.
    """

    def __init__(
        self,
        client: Client,
        path: str = "Authorization",
        _enc_key: bytes = b"$Dr@gonF!C0rP_Phil1ppin3s@2023#$",
        _enc_iv: bytes = b"0000000000000000",
    ):
        super().__init__(client, path)
        self._enc_key = _enc_key
        self._enc_iv = _enc_iv

    def login(self, username: str, password: str) -> LoginResponse:
        """Log in with username and password.

        Parameters
        ----------
        username : str
            The account username (email).
        password : str
            The plaintext password. It is encrypted before being sent.

        Returns
        -------
        LoginResponse
            The login response returned from the API.
        """
        payload = {
            "username": username,
            "password": self._encrypt_password(
                password, self._enc_key, self._enc_iv
            ),
        }
        return cast(LoginResponse, self._post("Login", payload))

    @staticmethod
    def _encrypt_password(password: str, enc_key: bytes, enc_iv: bytes) -> str:
        cipher = AES.new(enc_key, AES.MODE_CBC, iv=enc_iv)
        plaintext = json.dumps(password).encode("utf-8")
        ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
        return base64.b64encode(ciphertext).decode("utf-8")
