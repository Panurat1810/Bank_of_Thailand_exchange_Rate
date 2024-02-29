from dataclasses import dataclass
from datetime import date, datetime
from typing import Dict, List

import pandas as pd
import requests
from requests import Response

from Bank_of_Thailand_Exchange_Rate.currency_row import CurrencyRow
from Bank_of_Thailand_Exchange_Rate.request_config import (
    END_PERIOD,
    HEADERS,
    OUTPUT_PATH,
    START_PERIOD,
    URL,
)


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
            Process: Call API -> extract data -> return dataframe.
        :return: None.
        """
        response = Currency.get_exchange_rate()
        data_detail_list = Currency.get_currency_data(response=response)
        table = Currency.get_currency_table(data_detail_list=data_detail_list)
        Currency.to_parquet(table)
        # df = pd.DataFrame(table)
        # df = df.convert_dtypes()
        # df['period'] = pd.to_datetime(df['period']).dt.date.astype('datetime64[D]')
        # return df

    @staticmethod
    def get_exchange_rate() -> Response or None:
        """
        Get Exchange Rate Function, this function call API
        Returns:response of api in json format

        """
        payload = {"start_period": START_PERIOD, "end_period": END_PERIOD}
        response = requests.get(url=URL, params=payload, headers=HEADERS)
        if response.status_code == 200:
            return response
        else:
            return None

    @staticmethod
    def get_currency_row(tmp_dict: Dict[str, any]) -> CurrencyRow:
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
    def get_currency_data(response: Response) -> List[Dict[str, any]]:
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
                    data_detail_list = data_dict["data_detail"]
                    data_detail_list_cleaned = []
                    for data_detail_dict in data_detail_list:
                        convert_data_dict = Currency.convert_data_types(data_detail_dict)
                        data_detail_list_cleaned.append(convert_data_dict)
                    return data_detail_list_cleaned
                else:
                    raise KeyError("Key 'data_detail' is not found in data_dict")
            else:
                raise KeyError("Key 'data' is not found in result_dict")
        else:
            raise KeyError("Key 'result' is not found in response_dict")

    @staticmethod
    def convert_data_types(data_detail_dict: Dict[str, any]) -> Dict[str, any]:
        """
        Convert datatype of each element in dict
        Args:
            data_detail_dict: Dict[str, any]

        Returns: Dict[str, any]

        """
        converted_data_detail_dict = {}
        for key, value in data_detail_dict.items():
            # Replace empty strings with None
            if value == "":
                converted_data_detail_dict[key] = None
            elif key == "period":
                try:
                    converted_data_detail_dict[key] = datetime.strptime(value, "%Y-%m-%d").date()
                except ValueError:
                    converted_data_detail_dict[key] = None
            elif key in ["buying_sight", "buying_transfer", "mid_rate", "selling"]:
                try:
                    converted_data_detail_dict[key] = float(value)
                except ValueError:
                    converted_data_detail_dict[key] = None
            else:
                converted_data_detail_dict[key] = value
        return converted_data_detail_dict

    @staticmethod
    def get_currency_table(data_detail_list: List[Dict[str, any]]) -> List[CurrencyRow]:
        """
        This function format data to table format
        Args:
            data_detail_list: extracted data from get_currency_data

        Returns: table of extracted data

        """
        table: List[CurrencyRow] = []
        for data_detail_dict in data_detail_list:
            table.append(Currency.get_currency_row(data_detail_dict))
        return table

    @staticmethod
    def to_parquet(table: List[CurrencyRow]) -> None:
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
    def to_csv(table: List[CurrencyRow]) -> None:
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
