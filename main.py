import pandas as pd

from Bank_of_Thailand_Exchange_Rate.average_exchange_rate_thb import Currency

con = Currency()
df = con.pipeline()
