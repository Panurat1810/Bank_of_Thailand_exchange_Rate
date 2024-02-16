import unittest
from unittest.mock import MagicMock, patch

from Bank_of_Thailand_Exchange_Rate.average_exchange_rate_thb import Currency


class TestExchangeRate(unittest.TestCase):
    @patch("Bank_of_Thailand_Exchange_Rate.average_exchange_rate_thb.requests")
    def test_exchange_rate_success(self, mock_requests):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "result": {
                "timestamp": "test",
                "api": "test",
                "data": {
                    "data_detail": {
                        "period": "2024-02-16",
                        "currency_id": "test",
                        "currency_name_th": "test",
                        "currency_name_eng": "USA : DOLLAR (USD) ",
                        "buying_sight": "1.0",
                        "buying_transfer": "1.0",
                        "selling": "1.0",
                        "mid_rate": "1.0",
                    }
                },
            }
        }
        mock_requests.get.return_value = mock_response
        response = Currency.get_exchange_rate()
        currency_id = response.json()["result"]["data"]["data_detail"]
        self.assertEqual(currency_id["currency_id"], "test")

    @patch("Bank_of_Thailand_Exchange_Rate.average_exchange_rate_thb.requests")
    def test_exchange_rate_fail(self, mock_requests):
        mock_response = MagicMock()
        mock_response.status_code = 400

        mock_requests.get.return_value = mock_response
        self.assertIsNone(Currency.get_exchange_rate())
