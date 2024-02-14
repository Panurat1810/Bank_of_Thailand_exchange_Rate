from dataclasses import dataclass
import requests
from requests import Response
from Bank_of_Thailand_Exchange_Rate.config import (
    END_PERIOD,
    HEADERS,
    OUTPUT_PATH,
    START_PERIOD,
    URL,
)

@dataclass
class CurrencyRow:
    """
    Class that consists of exchange rate row attributes.
    """

    buying_sight: float
    buying_transfer: float
    currency_id: str
    currency_name_eng: str
    mid_rate: float
    period: str
    selling: float



