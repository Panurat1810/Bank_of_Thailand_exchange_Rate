from datetime import datetime
from Bank_of_Thailand_Exchange_Rate.average_exchange_rate_thb import Currency


class TestConvertDataTypes:

    @staticmethod
    def test_empty_string_conversion():
        data = {'key1': '', 'key2': 'value2', 'key3': ''}
        expected_output = {'key1': None, 'key2': 'value2', 'key3': None}
        assert Currency.convert_data_types(data) == expected_output

    @staticmethod
    def test_date_conversion():
        data = {'period': '2024-02-28', 'key2': 'value2'}
        expected_output = {'period': datetime(2024, 2, 28).date(), 'key2': 'value2'}
        assert Currency.convert_data_types(data) == expected_output

    @staticmethod
    def test_float_conversion():
        data = {'buying_sight': '35.7543000', 'key2': 'value2'}
        expected_output = {'buying_sight': 35.7543, 'key2': 'value2'}
        assert Currency.convert_data_types(data) == expected_output

    @staticmethod
    def test_invalid_date_conversion():
        data = {'period': 'invalid_date', 'key2': 'value2'}
        expected_output = {'period': None, 'key2': 'value2'}
        assert Currency.convert_data_types(data) == expected_output

    @staticmethod
    def test_invalid_float_conversion():
        data = {'buying_sight': 'invalid_float', 'key2': 'value2'}
        expected_output = {'buying_sight': None, 'key2': 'value2'}
        assert Currency.convert_data_types(data) == expected_output