from typing import cast

from httpx import Client

from dragonpy.responses.client_profile import GetClientAccountsResponse
from dragonpy.services.service import Service


class ClientProfileService(Service):
    """
    Service class for DragonFI REST API route /ClientProfile.
    """

    def __init__(self, client: Client, path: str = "ClientProfile") -> None:
        super().__init__(client, path)

    def get_client_accounts(
        self, isShowMetrics: bool = False, accountCode: str | None = None
    ) -> GetClientAccountsResponse:
        """Get the client's accounts.

        Parameters
        ----------
        accountCode : str, optional
            The account code to fetch.
        isShowMetrics : bool, optional
            Whether to include DX account metrics. Defaults to False.

        Returns
        -------
        GetClientAccountsResponse
            The client's accounts returned from the API.
        """
        params = {
            "isShowMetrics": isShowMetrics,
        }
        if isShowMetrics and accountCode is None:
            raise ValueError(
                "accountCode must be provied if isShowMetrics is `True`."
            )

        self._add_optional_params(params, accountCode=accountCode)
        return cast(
            GetClientAccountsResponse,
            self._get("GetClientAccounts", params),
        )
