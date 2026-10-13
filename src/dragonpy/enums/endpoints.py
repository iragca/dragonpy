from enum import StrEnum


class DragonFiEndpoint(StrEnum):
    REST_V1 = "https://api.dragonfi.ph/api/"
    REST_V2 = "https://api.dragonfi.ph/api/v2/"
    WSS = "wss://api.dragonfi.ph/"
