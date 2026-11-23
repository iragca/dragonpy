from .wrapper import DragonPy


class User(DragonPy):
    """
    DragonFi user account wrapper.
    Only accepts TOTP authentication for now.
    """

    def __init__(self, email: str, password: str, totp: str, **wrapper_kwargs):
        super().__init__(**wrapper_kwargs)
        self._login_totp(email, password, totp)

    def _login_totp(self, email: str, password: str, totp: str):
        token = self.authorization.get_anonymous_session()
        self._client.headers.update({"Authorization": f"Bearer {token}"})
        login_response = self.authorization.login(email, password)
        self._client.headers.update(
            {"Authorization": f"Bearer {login_response['loginToken']}"}
        )
        verify_response = self.clients.verify_totp(email, totp)
        self._client.headers.update(
            {"Authorization": f"Bearer {verify_response['token']}"}
        )
