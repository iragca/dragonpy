from http import HTTPStatus

from .http import HTTPException


class FundNotFoundError(HTTPException):
    def __init__(self, fund_code: str) -> None:
        super().__init__(
            status_code=HTTPStatus.NOT_FOUND,
            detail=f"Fund not found: {fund_code}",
        )
