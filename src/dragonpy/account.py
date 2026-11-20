from .wrapper import DragonPy


class Account:
    """
    DragonFi account wrapper.
    Only accepts TOTP authentication for now.
    """

    def __init__(self, email: str, password: str, totp: str, **wrapper_kwargs):
        self.dpy = DragonPy(**wrapper_kwargs)
        self._login_totp(email, password, totp)

    def _login_totp(self, email: str, password: str, totp: str):
        token = self.dpy.authorization.get_anonymous_session()
        self.dpy._client.headers.update({"Authorization": f"Bearer {token}"})
        login_response = self.dpy.authorization.login(email, password)
        self.dpy._client.headers.update(
            {"Authorization": f"Bearer {login_response['loginToken']}"}
        )
        verify_response = self.dpy.clients.verify_totp(email, totp)
        self.dpy._client.headers.update(
            {"Authorization": f"Bearer {verify_response['token']}"}
        )
