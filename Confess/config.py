import os
import logging
from os import getenv
from logging.handlers import RotatingFileHandler
from dotenv import load_dotenv

load_dotenv(".env")

API_ID = getenv("API_ID", "20211998")
API_HASH = getenv("API_HASH", "beeeebe74c0c467c47c6ac4a1c9d75b5")
BOT_TOKEN = getenv("BOT_TOKEN", "")

SESSION = getenv("SESSION", "")
BOT_WORKERS = getenv("BOT_WORKERS", "4")
