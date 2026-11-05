from json import loads
from typing import Any
from urllib.parse import urlencode

from httpx import Client

from dragonpy.enums import HTTPStatus
from dragonpy.exceptions import HTTPException
from dragonpy.utils import merge_url


class Service:
    """
    The base class for implementing services of the DragonFI API.

    Attributes
    ----------
    client : httpx.Client
        The HTTP client to perform HTTP requests, connections
        and sessions.
    service_url : str
        The route's base url. i.e `https://api.dragonfi.ph/v2/Route/`.

    Notes
    -----
    Parameter names are made to mimick the API function names to
    minimize confusion and ambiguity, regardless if they don't adhere
    to Python's PEP8 standards.
    """

    def __init__(self, client: Client, path: str):
        self.client: Client = client
        self.service_url: str = merge_url(str(client.base_url), path)

    def _get(
        self, function: str, params: dict[str, str | int]
    ) -> dict[str, str | int | float] | str | list[Any]:
        """HTTP GET wrapper

        Parameters
        ----------
        function : str
            The route function. i.e /Route/<function>.
        params : dict[str, str | int | float]
            The query parameters to encode with request.

        Returns
        -------
        dict[str, str | int | float] | str | list[Any]
            The parsed JSON response from the API.

        Raises
        ------
        HTTPException
            If the response status code is categorically unsuccessful.
        """
        base_url = merge_url(self.service_url, function)
        queries = urlencode(params)
        req_url = f"{base_url}?{queries}"
        response = self.client.get(req_url)
        status = HTTPStatus(response.status_code)
        if status.is_success:
            if response.content == b"":
                return {}

            return loads(response.content)

        if response.content == b"":
            detail = req_url
        else:
            detail = f"[{req_url}] {response.content}"

        raise HTTPException(response.status_code, detail=detail)

    @staticmethod
    def _add_optional_params(
        params: dict[str, str | int | float]
        | dict[str, str]
        | dict[str, int]
        | dict[str, str | int]
        | dict[str, int | float]
        | dict[str, float]
        | dict[str, float | int]
        | dict[str, float | str],
        **kwargs,
    ) -> None:
        """Adds a query parameter to an existing URL query dictionary
        if its value is not `None`.

        Parameters
        ----------
        params : dict[str, str | int | float]
        | dict[str, str]
        | dict[str, int]
        | dict[str, str | int]
        | dict[str, int | float]
        | dict[str, float]
        | dict[str, float | int]
        | dict[str, float | str]
        TODO: Simplify types so the linter doesn't go crazy.
            The URL query dictionary.
        **kwargs
            The query key and value pairs.
        """
        for key, value in kwargs.items():
            if value is not None:
                params[key] = value
