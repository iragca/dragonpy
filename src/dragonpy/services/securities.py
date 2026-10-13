from json import loads
from typing import cast
from urllib.parse import urlencode

from httpx import get

from dragonpy.enums import HTTPStatus
from dragonpy.exceptions import HTTPException
from dragonpy.responses.securities import GetStockProfile
from dragonpy.utils import merge_url


class SecuritiesService:
    def __init__(self, base_url: str, path: str = "Securities"):
        self.service_url: str = merge_url(base_url, path)

    def get_stock_profile(self, stockCode: str) -> GetStockProfile:
        return cast(
            GetStockProfile,
            self._get("GetStockProfile", {"stockCode": stockCode}),
        )

    def _get(self, function: str, params: dict[str, str]) -> object:
        base_url = merge_url(self.service_url, function)
        queries = urlencode(params)
        req_url = f"{base_url}?{queries}"
        response = get(req_url)
        status = HTTPStatus(response.status_code)
        if status.is_success:
            return loads(response.content)

        raise HTTPException(response.status_code, detail=req_url)
