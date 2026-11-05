from pytest import fixture, raises

from dragonpy.exceptions.funds import FundNotFoundError
from dragonpy.responses.funds import GetFund
from dragonpy.services import FundsService


@fixture(scope="class")
def service(client):
    return FundsService(client)


class TestFundsServices:
    def test_get_fund(self, service: FundsService):
        data: GetFund = service.get_fund("BPIEF5")
        assert isinstance(data, dict), data
        assert "fundName" in data

    def test_fake_fund(self, service: FundsService):
        ticker = "FAKEFUND"
        with raises(FundNotFoundError):
            service.get_fund(ticker)

        with raises(FundNotFoundError):
            service.get_fund_navpu(ticker)

        with raises(FundNotFoundError):
            service.get_related_funds(ticker)

    def test_limit_positive(self, service: FundsService):
        with raises(ValueError, match="nonnegative"):
            service.get_related_funds("BPIEF5", limit=-1)

    def test_get_fund_paged_list(self, service: FundsService):
        search_term = "bpi"

        # No exceptions, all status 200
        service.get_fund_paged_list(search_term, FilterBy="fundManager")
        service.get_fund_paged_list(search_term, FilterBy="fundName")
        service.get_fund_paged_list(search_term, FilterBy="fundCode")
        service.get_fund_paged_list(search_term, FilterBy="bloombergTicker")
        service.get_fund_paged_list(search_term, SortBy="return1yr")
        service.get_fund_paged_list(search_term, SortBy="return1yrPercent")
        service.get_fund_paged_list(search_term, SortBy="return3yr")
        service.get_fund_paged_list(search_term, SortBy="currentNAVPU")
        service.get_fund_paged_list(search_term, SortBy="return3yrPercent")
        service.get_fund_paged_list(search_term, RiskClassification=1)
        service.get_fund_paged_list(search_term, RiskClassification=2)
        service.get_fund_paged_list(search_term, RiskClassification=3)
        service.get_fund_paged_list(search_term, isPera=True)
        service.get_fund_paged_list(search_term, isPera=False)
