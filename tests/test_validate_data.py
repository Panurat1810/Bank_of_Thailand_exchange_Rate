import pytest

from Bank_of_Thailand_Exchange_Rate.average_exchange_rate_thb import Currency


@pytest.fixture
def std_currency_names() -> tuple[list[str], list[str]]:
    obj = Currency()
    response = obj.get_exchange_rate()
    df = response.json()
    currency_id = []
    currency_name_eng = []
    for item in df["result"]["data"]["data_detail"]:
        currency_id.append(item["currency_id"])
        currency_name_eng.append(item["currency_name_eng"])
    return currency_name_eng, currency_id


def test_validate_data_currency_success(
        mock_good_data: dict[str, any], std_currency_names: tuple[list[str], list[str]]) -> None:
    currency_name, currency_id = std_currency_names
    assert mock_good_data["currency_id"] in currency_id
    assert mock_good_data["currency_name_eng"] in currency_name


def test_validate_data_currency_failed(
        mock_bad_data: dict[str, any], std_currency_names: tuple[list[str], list[str]]) -> None:
    currency_name, currency_id = std_currency_names
    assert mock_bad_data["currency_id"] not in currency_id
    assert mock_bad_data["currency_name_eng"] not in currency_name
