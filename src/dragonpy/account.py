from dragonpy.data.account import Fund, Stock

from .wrapper import DragonPy


class User:
    """
    DragonFi user account wrapper.
    Only accepts TOTP authentication for now.
    """

    def __init__(self, email: str, password: str, totp: str, **wrapper_kwargs):
        self._dpy = DragonPy(**wrapper_kwargs)
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
        token = self._dpy.authorization.get_anonymous_session()
        self._dpy._client.headers.update({"Authorization": f"Bearer {token}"})
        login_response = self._dpy.authorization.login(email, password)
        self._dpy._client.headers.update(
            {"Authorization": f"Bearer {login_response['loginToken']}"}
        )
        verify_response = self._dpy.clients.verify_totp(email, totp)
        self._dpy._client.headers.update(
            {"Authorization": f"Bearer {verify_response['token']}"}
        )

    def _accounts_with_metrics(self):
        accounts = self._dpy.client_profile.get_client_accounts()
        return [
            self._dpy.client_profile.get_client_accounts(
                isShowMetrics=True,
                accountCode=a["accountCode"].replace("default:", ""),
            )[0]
            for a in accounts
        ]

    @property
    def stocks(self) -> list[Stock]:
        """Get the user's stock positions across all accounts.

        Returns
        -------
        list[Stock]
            Stock positions from every account with metrics enabled.
        """
        stocks = []
        for account in self._accounts_with_metrics():
            metrics = account.get("dxAccountMetrics", {}).get(  # ty: ignore[missing-union-attribute]
                "metrics", []
            )
            if not metrics:
                continue
            for p in metrics[0]["positions"]:
                stocks.append(
                    Stock(
                        symbol=p["symbol"],
                        average_price=p["averagePrice"],
                        quantity=p["quantity"],
                        rate=p["rate"],
                        market_value=p["marketValue"],
                        gross_amount=p["grossAmount"],
                        pct_gain_loss=p["percentGainLoss"],
                    )
                )
        return stocks

    @property
    def funds(self) -> list[Fund]:
        """Get the user's fund positions across all accounts.

        Returns
        -------
        list[Fund]
            Fund positions from every account.
        """
        funds = []
        for account in self._dpy.client_profile.get_client_accounts():
            fund_positions = self._dpy.funds.get_fund_position_page_list(
                account["accountCode"]
            ).get("fundPositionList", [])
            for f in fund_positions:
                funds.append(
                    Fund(
                        code=f["fundCode"],
                        name=f["fundName"],
                        id=f["fundId"],
                        unit=f["unit"],
                        average_price=f["avgPrice"],
                        gross_amount=f["grossAmount"],
                        current_navpu=f["currentNAVPU"],
                        market_value=f["marketValue"],
                    )
                )
        return funds
