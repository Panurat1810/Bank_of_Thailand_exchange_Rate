from dataclasses import dataclass
from datetime import date


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
    period: date
    selling: float
