from json import loads
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
    """

    def __init__(self, client: Client, path: str):
        self.client: Client = client
        self.service_url: str = merge_url(str(client.base_url), path)

    def _get(self, function: str, params: dict[str, str | int]) -> dict:
        """HTTP GET wrapper

        Parameters
        ----------
        function : str
            The route function. i.e /Route/<function>.
        params : dict[str, str | int]
            The query parameters to encode with request.

        Returns
        -------
        dict
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

        raise HTTPException(response.status_code, detail=req_url)
