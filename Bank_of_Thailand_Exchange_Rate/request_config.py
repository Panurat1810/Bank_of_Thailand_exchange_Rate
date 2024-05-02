import json
import os
from datetime import date, timedelta
from airflow.models import Variable


URL: str = "https://apigw1.bot.or.th/bot/public/Stat-ExchangeRate/v2/DAILY_AVG_EXG_RATE/"
today = date.today()
START_PERIOD: str = (today - timedelta(days=5)).isoformat()
END_PERIOD: str = today.isoformat()
KEY: str = Variable.get('API_KEY') if Variable.get('API_KEY') else "" or None

env_var_value = Variable.get('API_HEADERS')
if env_var_value:
    HEADERS = json.loads(env_var_value)
else:
    HEADERS = None

OUTPUT_PATH: str = Variable.get('OUTPUT') if Variable.get('OUTPUT') else "" or None





