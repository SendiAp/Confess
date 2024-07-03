import os
import logging
from os import getenv
from logging.handlers import RotatingFileHandler
from dotenv import load_dotenv

load_dotenv(".env")

API_ID = getenv("API_ID", "20211998")
API_HASH = getenv("API_HASH", "beeeebe74c0c467c47c6ac4a1c9d75b5")

BOT_TOKEN = getenv("BOT_TOKEN", "")
BOT_USERNAME = getenv("BOT_USERNAME", "")

MONGO_DB_URL = getenv("MONGO_DB_URL", "")
DB_NAME = getenv("DB_NAME", "khodam")

FORCE_SUB_CHANNEL = getenv("FORCE_SUB_CHANNEL", "")
FORCE_SUB_GROUP = getenv("FORCE_SUB_GROUP", "")

OWNER_ID = getenv("OWNER_ID", "")

BROADCAST_AS_COPY = True

SESSION = getenv("SESSION", "")
BOT_WORKERS = getenv("BOT_WORKERS", "4")

LOG_FILE_NAME = "kantorpos.txt"
logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=50000000, backupCount=10),
        logging.StreamHandler(),
    ],
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
