from datetime import date
from typing import Dict, List

import pytest

from Bank_of_Thailand_Exchange_Rate.currency_row import CurrencyRow


@pytest.fixture()
def mock_good_data() -> Dict[str, any]:
    return {
        "buying_sight": 1.0,
        "buying_transfer": 1.0,
        "currency_id": "USD",
        "currency_name_eng": "USA : DOLLAR (USD) ",
        "mid_rate": 1.0,
        "period": date(2024, 2, 8),
        "selling": 1.0,
    }


@pytest.fixture()
def mock_list_good_data() -> List[Dict[str, any]]:
    return [
        {
            "buying_sight": 1.0,
            "buying_transfer": 1.0,
            "currency_id": "USD",
            "currency_name_eng": "USA : DOLLAR (USD) ",
            "mid_rate": 1.0,
            "period": date(2024, 2, 8),
            "selling": 1.0,
        }
    ]


@pytest.fixture()
def mock_bad_data() -> Dict[str, any]:
    return {
        "buying_sight": 1,
        "buying_transfer": 1,
        "currency_id": "USA",
        "currency_name_eng": "USD : DOLLAR (USD)",
        "mid_rate": 1,
        "period": date(2024, 2, 8),
        "selling": 1.0,
    }


@pytest.fixture()
def mock_invalid_data() -> Dict[str, any]:
    return {
        "buy_sight": 1,
        "buy_transfer": 1,
        "currency_id": "USA",
        "currency_name_eng": "USD : DOLLAR (USD)",
        "mid_rate": 1,
        "period": date(2024, 2, 8),
        "selling": 1.0,
    }


@pytest.fixture()
def mock_good_data_good_currency_row(mock_good_data: Dict[str, any]) -> CurrencyRow:
    mock_currency_row: CurrencyRow = CurrencyRow(
        buying_sight=mock_good_data["buying_sight"],
        buying_transfer=mock_good_data["buying_transfer"],
        currency_id=mock_good_data["currency_id"],
        currency_name_eng=mock_good_data["currency_name_eng"],
        mid_rate=mock_good_data["mid_rate"],
        period=mock_good_data["period"],
        selling=mock_good_data["selling"],
    )
    return mock_currency_row


@pytest.fixture()
def mock_invalid_row(mock_invalid_data: Dict[str, any]) -> Dict[str, any]:
    mock_currency_row = {
        "buy_sight": mock_invalid_data["buy_sight"],
        "buy_transfer": mock_invalid_data["buy_transfer"],
        "currency_id": mock_invalid_data["currency_id"],
        "currency_name_eng": mock_invalid_data["currency_name_eng"],
        "mid_rate": mock_invalid_data["mid_rate"],
        "period": mock_invalid_data["period"],
        "selling": mock_invalid_data["selling"],
    }
    return mock_currency_row


@pytest.fixture()
def mock_bad_data_good_currency_row(mock_bad_data: Dict[str, any]) -> CurrencyRow:
    mock_currency_row: CurrencyRow = CurrencyRow(
        buying_sight=mock_bad_data["buying_sight"],
        buying_transfer=mock_bad_data["buying_transfer"],
        currency_id=mock_bad_data["currency_id"],
        currency_name_eng=mock_bad_data["currency_name_eng"],
        mid_rate=mock_bad_data["mid_rate"],
        period=mock_bad_data["period"],
        selling=mock_bad_data["selling"],
    )
    return mock_currency_row
