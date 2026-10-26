from json import loads
from urllib.parse import urlencode

from httpx import Client

from dragonpy.enums import HTTPStatus
from dragonpy.exceptions import HTTPException
from dragonpy.utils import merge_url


class Service:
    def __init__(self, client: Client, path: str):
        self.client: Client = client
        self.service_url: str = merge_url(str(client.base_url), path)

    def _get(self, function: str, params: dict[str, str | int]) -> dict:
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
