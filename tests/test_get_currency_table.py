from typing import Dict, List, NoReturn

from Bank_of_Thailand_Exchange_Rate.average_exchange_rate_thb import Currency
from Bank_of_Thailand_Exchange_Rate.currency_row import CurrencyRow


def test_get_currency_table_success(mock_list_good_data: List[Dict[str, any]]) -> NoReturn:
    result = Currency.get_currency_table(mock_list_good_data)
    assert isinstance(result, list)
    for key in result:
        assert isinstance(key, CurrencyRow)


def test_get_currency_table_failed() -> NoReturn:
    result = Currency.get_currency_table([])
    assert result == []
