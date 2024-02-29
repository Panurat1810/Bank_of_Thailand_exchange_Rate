from Bank_of_Thailand_Exchange_Rate.average_exchange_rate_thb import Currency
import pandas as pd

con = Currency()
df = con.pipeline()
