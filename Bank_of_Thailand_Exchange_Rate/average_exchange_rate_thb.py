from dataclasses import dataclass
from datetime import date

import pandas as pd
import requests
from requests import Response

from Bank_of_Thailand_Exchange_Rate.config import (
    END_PERIOD,
    HEADERS,
    OUTPUT_PATH,
    START_PERIOD,
    URL,
)
from Bank_of_Thailand_Exchange_Rate.currency_row import CurrencyRow


@dataclass
class Currency:
    """
    This class purpose is dto acquire money exchange rate
    from Bank of Thailand.
    """

    @staticmethod
    def pipeline() -> None:
        """
            This is a Currency Exchange Pipeline,a main function.
            Process: Call API -> extract data -> Write file.
        :return: None.
        """
        response = Currency.get_exchange_rate(number=1)
        detail_data_dict = Currency.get_currency_data(response=response)
        table = Currency.get_currency_table(data_detail_dict=detail_data_dict)
        Currency.to_parquet(table=table)

    @staticmethod
    def get_exchange_rate(number: int) -> Response | None:
        """
        Get Exchange Rate Function, this function call API
        Returns:response of api in json format

        """
        if number == 1:
            payload = {"start_period": START_PERIOD, "end_period": END_PERIOD}
            response = requests.get(url=URL, params=payload, headers=HEADERS)
            #        print("Status Code", response.status_code)
            #        print("JSON Response ",json.dumps(response.json(),indent=4))
            if response.status_code == 200:
                return response
            else:
                return None
        if number == 2:
            payload = {"start_period": START_PERIOD, "end_period": END_PERIOD}
            response = requests.get(url=URL, params=payload, headers=HEADERS)
            #        print("Status Code", response.status_code)
            #        print("JSON Response ",json.dumps(response.json(),indent=4))
            if response.status_code == 200:
                return response.json()["result"]["data"]["data_detail"]["currency_id"]
            else:
                return None

    @staticmethod
    def get_currency_row(tmp_dict: dict[str, any]) -> CurrencyRow:
        """
            Get Currency Row.
        :param tmp_dict: Temporary Dict represent a record of currency exchange
            tmp_dict['buying_sight']:Thai Baht
            tmp_dict['buying_transfer']:Thai Baht
            tmp_dict['currency_id']: Currency ID
            tmp_dict['currency_name_eng']: Currency Name
            tmp_dict['mid_rate']:Thai Baht
            tmp_dict['period']:Occurring Date
            tmp_dict['selling']:Thai Baht
        :return: CurrencyRow
        """
        return CurrencyRow(
            buying_sight=tmp_dict["buying_sight"],
            buying_transfer=tmp_dict["buying_transfer"],
            currency_id=tmp_dict["currency_id"],
            currency_name_eng=tmp_dict["currency_name_eng"],
            mid_rate=tmp_dict["mid_rate"],
            period=tmp_dict["period"],
            selling=tmp_dict["selling"],
        )

    @staticmethod
    def get_currency_data(response: Response) -> list[dict[str, any]]:
        """
        This function extracts data from response
        Args:
            response:response from API

        Returns: data_detail_dict: extracted Data

        """
        response_dict = response.json()
        if "result" in response_dict:
            result_dict = response_dict["result"]
            if "data" in result_dict:
                data_dict = result_dict["data"]
                if "data_detail" in data_dict:
                    data_detail_dict = data_dict["data_detail"]
                    return data_detail_dict
                else:
                    raise KeyError("Key 'data_detail' is not found in data_dict")
            else:
                raise KeyError("Key 'data' is not found in result_dict")
        else:
            raise KeyError("Key 'result' is not found in response_dict")

    @staticmethod
    def get_currency_table(data_detail_dict: list[dict[str, any]]) -> list[CurrencyRow]:
        """
        This function format data to table format
        Args:
            data_detail_dict:extracted data from get_currency_data

        Returns: table of extracted data

        """
        table: list[CurrencyRow] = []
        for key in data_detail_dict:
            table.append(Currency.get_currency_row(key))
        return table

    @staticmethod
    def to_parquet(table: list[CurrencyRow]) -> None:
        """
        This method is to format a table of extracted data to CSV
        Args:
            table:extracted data of exchange rate

        Returns: none

        """
        try:
            df = pd.DataFrame(table)
            datetime_suffix: str = date.today().strftime("%Y%m%d")
            df.to_parquet(
                f"{OUTPUT_PATH}exchange_rates_{datetime_suffix}.parquet",
                index=False,
            )
        except OSError:
            raise OSError

    @staticmethod
    def to_csv(table: list[CurrencyRow]) -> None:
        """
        This method is to format a table of extracted data to CSV
        Args:
            table:extracted data of exchange rate

        Returns: none

        """
        try:
            df = pd.DataFrame(table)
            datetime_suffix: str = date.today().strftime("%Y%m%d")
            df.to_csv(
                f"{OUTPUT_PATH}exchange_rates_{datetime_suffix}.csv",
                index=False,
                sep=",",
                encoding="utf-8",
            )
        except OSError:
            raise OSError
