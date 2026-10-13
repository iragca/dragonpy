from dragonpy.utils import merge_url

class FundsService:
    def __init__(self, base_url: str, path: str = "Funds"):
        self.request_url: str = merge_url(base_url, path)
