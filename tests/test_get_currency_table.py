from Bank_of_Thailand_Exchange_Rate.average_exchange_rate_thb import Currency
from Bank_of_Thailand_Exchange_Rate.currency_row import CurrencyRow


def test_get_currency_table_success(mock_list_good_data: list[dict[str, any]]) -> None:
    result = Currency.get_currency_table(mock_list_good_data)
    assert isinstance(result, list)
    for key in result:
        assert isinstance(key, CurrencyRow)


def test_get_currency_table_failed() -> None:
    result = Currency.get_currency_table([])
    assert result == []
