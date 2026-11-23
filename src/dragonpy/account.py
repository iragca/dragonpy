from dragonpy.data import Account
from dragonpy.enums.dragonfi import PlanType

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
        """Login with Password and TOTP (Timed One-Time-Password).

        Parameters
        ----------
            email: str
                The user's registered email.
            password: str
                The user's registered password.
            totp: str
                The user's configured 6 digit TOTP.
        """
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

    @property
    def accounts(self) -> list[Account]:
        accounts = self.client_profile.get_client_accounts()

        accounts_with_metrics = []
        for a in accounts:
            acc = self.client_profile.get_client_accounts(
                isShowMetrics=True,
                accountCode=a["accountCode"].replace("default:", ""),
            )
            accounts_with_metrics.append(acc[0])

        return [
            Account(
                id=a["id"],
                account_code=a["accountCode"],
                alias=a["accountAlias"],
                plan=PlanType(a["planTypeId"]),
                equity=a.get("dxAccountMetrics", {})  # ty: ignore[missing-union-attribute]
                .get("metrics", [{"equity": 0}])[0]
                .get("equity"),
            )
            for a in accounts_with_metrics
        ]
