from datetime import date
from typing import Dict, NoReturn

from Bank_of_Thailand_Exchange_Rate.currency_row import CurrencyRow


def test_validate_type_currency_row_success(mock_good_data_good_currency_row: CurrencyRow) -> NoReturn:
    assert isinstance(mock_good_data_good_currency_row, CurrencyRow) is True


def test_validate_type_currency_row_failed(mock_invalid_row: Dict[str, any]) -> NoReturn:
    assert isinstance(mock_invalid_row, CurrencyRow) is False


def test_validate_attribute_currency_row_success(mock_good_data_good_currency_row: CurrencyRow) -> NoReturn:
    assert isinstance(mock_good_data_good_currency_row.buying_sight, float) is True
    assert isinstance(mock_good_data_good_currency_row.buying_transfer, float) is True
    assert isinstance(mock_good_data_good_currency_row.currency_id, str) is True
    assert isinstance(mock_good_data_good_currency_row.currency_name_eng, str) is True
    assert isinstance(mock_good_data_good_currency_row.mid_rate, float) is True
    assert isinstance(mock_good_data_good_currency_row.period, date) is True
    assert isinstance(mock_good_data_good_currency_row.selling, float) is True


def test_validate_attribute_currency_row_failed(mock_bad_data_good_currency_row: CurrencyRow) -> NoReturn:
    any_assertion_passed = False
    if not isinstance(mock_bad_data_good_currency_row.buying_sight, float):
        any_assertion_passed = True
    if not isinstance(mock_bad_data_good_currency_row.buying_transfer, float):
        any_assertion_passed = True
    if not isinstance(mock_bad_data_good_currency_row.currency_id, str):
        any_assertion_passed = True
    if not isinstance(mock_bad_data_good_currency_row.currency_name_eng, str):
        any_assertion_passed = True
    if not isinstance(mock_bad_data_good_currency_row.mid_rate, float):
        any_assertion_passed = True
    if not isinstance(mock_bad_data_good_currency_row.period, date):
        any_assertion_passed = True
    if not isinstance(mock_bad_data_good_currency_row.selling, float):
        any_assertion_passed = True

    assert any_assertion_passed, "All assertions failed"
