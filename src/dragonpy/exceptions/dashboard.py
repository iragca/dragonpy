from http import HTTPStatus

from .http import HTTPException


class SymbolNotFoundError(HTTPException):
    def __init__(self, symbol: str) -> None:
        super().__init__(
            status_code=HTTPStatus.NOT_FOUND,
            detail=f"Symbol not found: {symbol}",
        )
