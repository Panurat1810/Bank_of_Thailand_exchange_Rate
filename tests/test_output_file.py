import glob
import os.path
from unittest.mock import patch

import pytest

from Bank_of_Thailand_Exchange_Rate.average_exchange_rate_thb import Currency
from Bank_of_Thailand_Exchange_Rate.currency_row import CurrencyRow


def test_create_csv_file_success(mock_good_data: list[CurrencyRow]) -> None:
    obj = Currency()
    mock_table = list(mock_good_data)
    obj.to_csv(mock_table)
    csv_file = glob.glob("outputs/*.csv")
    assert len(csv_file) > 0
    for file in csv_file:
        os.remove(file)


@patch("Bank_of_Thailand_Exchange_Rate.average_exchange_rate_thb.pd.DataFrame.to_csv")
def test_create_csv_file_failed(mock_to_csv, mock_good_data: list[CurrencyRow]) -> None:
    mock_to_csv.side_effect = OSError("Mocked OSError")
    obj = Currency()
    mock_table = list(mock_good_data)
    with pytest.raises(OSError):
        obj.to_csv(mock_table)
        csv_file = glob.glob("outputs/*.csv")
        assert len(csv_file) == 0


def test_create_parquet_file_success(mock_good_data: list[CurrencyRow]) -> None:
    obj = Currency()
    mock_table = list(mock_good_data)
    obj.to_parquet(mock_table)
    parquet_file = glob.glob("outputs/*.parquet")
    assert len(parquet_file) > 0
    for file in parquet_file:
        os.remove(file)


@patch("Bank_of_Thailand_Exchange_Rate.average_exchange_rate_thb.pd.DataFrame.to_parquet")
def test_create_parquet_file_failed(mock_to_parquet, mock_good_data: list[CurrencyRow]) -> None:
    mock_to_parquet.side_effect = OSError("Mocked OSError")
    obj = Currency()
    mock_table = list(mock_good_data)
    with pytest.raises(OSError):
        obj.to_parquet(mock_table)
        parquet_file = glob.glob("outputs/*.parquet")
        assert len(parquet_file) == 0
