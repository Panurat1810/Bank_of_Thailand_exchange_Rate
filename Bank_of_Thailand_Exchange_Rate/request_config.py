import os
from typing import Dict

# this file is for api argument configuration

URL: str = "https://apigw1.bot.or.th/bot/public/Stat-ExchangeRate/v2/DAILY_AVG_EXG_RATE/"
START_PERIOD: str = "2024-02-01"
END_PERIOD: str = "2024-02-11"
KEY: str = os.getenv('API_KEY') if os.getenv('API_KEY') else "" or None
HEADERS = os.getenv('API_HEADERS') if os.getenv('API_HEADERS') else "" or None
OUTPUT_PATH: str = os.getenv('OUTPUT') if os.getenv('OUTPUT') else "" or None
