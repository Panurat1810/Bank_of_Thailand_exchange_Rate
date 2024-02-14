import pytest
from Bank_of_Thailand_Exchange_Rate.currency_row import CurrencyRow


@pytest.fixture
def mock_good_data() -> dict[str, any]:
    return {
        'buying_sight': 1.0,
        'buying_transfer': 1.0,
        'currency_id': "GC",
        'currency_name_eng': "GOOD CURRENCY",
        'mid_rate': 1.0,
        'period': "2022-02-14",
        'selling': 1.0,
    }


@pytest.fixture
def std_currency_name() -> list[str]:
    return ["USD"]


@pytest.fixture
def mock_good_currency_row(mock_good_data: dict[str, any]) -> CurrencyRow:
    mock_currency_row: CurrencyRow = CurrencyRow(
        buying_sight=mock_good_data['buying_sight'],
        buying_transfer=mock_good_data['buying_transfer'],
        currency_id=mock_good_data['currency_id'],
        currency_name_eng=mock_good_data['currency_name_eng'],
        mid_rate=mock_good_data['mid_rate'],
        period=mock_good_data['period'],
        selling=mock_good_data['selling']
    )
    return mock_currency_row


def test_validate_type_currency_row(mock_good_currency_row: CurrencyRow):
    assert isinstance(mock_good_currency_row, CurrencyRow) is True


def test_validate_attribute_currency_row(mock_good_currency_row: CurrencyRow):
    assert isinstance(mock_good_currency_row.buying_sight, float) is True
    assert isinstance(mock_good_currency_row.buying_transfer, float) is True
    assert isinstance(mock_good_currency_row.currency_id, str) is True
    assert isinstance(mock_good_currency_row.currency_name_eng, str) is True
    assert isinstance(mock_good_currency_row.mid_rate, float) is True
    assert isinstance(mock_good_currency_row.period, str) is True
    assert isinstance(mock_good_currency_row.selling, float) is True
