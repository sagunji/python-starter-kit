import os
from dotenv import load_dotenv

load_dotenv()

LOG_LEVEL = os.getenv("LOG_LEVEL", "info").lower()
LOG_LOCATION = os.getenv("LOG_LOCATION", "logs").lower()

APP_SETTINGS = os.getenv("APP_SETTINGS", "config.DevelopmentConfig")

