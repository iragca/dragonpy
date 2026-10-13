from .service import Service


class FundsService(Service):
    def __init__(self, base_url: str, path: str = "Funds"):
        super().__init__(base_url, path)
