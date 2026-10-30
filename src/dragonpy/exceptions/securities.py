from http import HTTPStatus

from .http import HTTPException


class StockNotFoundError(HTTPException):
    def __init__(self, stock_code: str) -> None:
        super().__init__(
            status_code=HTTPStatus.NOT_FOUND,
            detail=f"Stock not found: {stock_code}",
        )
