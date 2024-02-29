from os.path import dirname, join

# this file is for api argument configuration

URL: str = "https://apigw1.bot.or.th/bot/public/Stat-ExchangeRate/v2/DAILY_AVG_EXG_RATE/"
START_PERIOD: str = "2024-02-01"
END_PERIOD: str = "2024-02-11"
KEY: str = "yQ4dA1xB8wS5pP8kP0nH6oE8gE5sW8qC0eG4fT1tU7eP8pB3kF"
HEADERS = {"X-IBM-Client-Id": "c61c860d-1278-449d-923f-e51eb71452d5"}
OUTPUT_PATH: str = "/opt/airflow/dags/outputs/"
