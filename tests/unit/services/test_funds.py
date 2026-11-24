from unittest.mock import Mock

from pytest import fixture

from dragonpy.services import FundsService


@fixture
def service():
    client = Mock()
    client.base_url = "https://devtest.dragonfi.ph"
    return FundsService(client)


def test_get_fund_position_page_list(service: FundsService):
    response = {
        "fundPositionList": [
            {
                "accountCode": "EP-251217-16024",
                "fundCode": "BPIEF5",
                "fundName": "BPI US Equity Index Feeder Fund - PHP",
                "precision": 4,
                "fundId": 27,
                "fundLogoPath": (
                    "https://public-assets.dragonfi.ph/Securities/BPI/BPI"
                ),
                "unit": 29.2468,
                "avgPrice": 290.6301,
                "grossAmount": 8500.0000,
                "currentNAVPU": 290.1700,
                "currentNAVPUDate": "2026-11-23T00:00:00",
                "marketValue": 8486.5440,
                "unrealizedPL": -13.4565,
                "unrealizedPLPercent": -0.1586,
            }
        ],
        "totalCount": 1,
    }
    service._get = Mock(return_value=response)

    data = service.get_fund_position_page_list("EP-251217-16024")

    assert data == response

    args, _kwargs = service._get.call_args
    assert args[0] == "GetFundPositionPagedList"
    assert args[1] == {
        "AccountCode": "EP-251217-16024",
        "Asc": "false",
        "IsPaged": "false",
    }


def test_get_fund_position_page_list_params(service: FundsService):
    service._get = Mock(return_value={"fundPositionList": [], "totalCount": 0})

    service.get_fund_position_page_list("EP-251217-16024", True, True)

    args, _kwargs = service._get.call_args
    assert args[1]["Asc"] == "true"
    assert args[1]["IsPaged"] == "true"
