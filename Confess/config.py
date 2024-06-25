import os
import logging
from os import getenv
from logging.handlers import RotatingFileHandler
from dotenv import load_dotenv

load_dotenv(".env")

BOT_TOKEN = getenv("BOT_TOKEN", "")
