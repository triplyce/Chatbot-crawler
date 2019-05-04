import os

from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
HTTP_REDDIT_URL = os.getenv("BASE_HTTP_URL")
