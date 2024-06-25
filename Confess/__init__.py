import sys
import asyncio
import os
import pytz

from pyromod import listen
from pyrogram import *
from pyrogram.errors import FloodWait
from pyrogram.types import *
from pyrogram import __version__

from Confess.config import *


class Bot(Client):
    def __init__(self):
        super().__init__(
            "Bot",
            api_hash=API_HASH,
            api_id=API_ID,
            plugins={"root": "Confess/modules"},
            workers=4,
            bot_token=BOT_TOKEN,
        )
        self.LOGGER = LOGGER

    async def start(self):
        try:
            await super().start()
            usr_bot_me = await self.get_me()
            self.username = usr_bot_me.username
            self.namebot = usr_bot_me.first_name
            self.LOGGER(__name__).info(
                f"TG_BOT_TOKEN detected!\n┌ First Name: {self.namebot}\n└ Username: @{self.username}"
            )
        except Exception as a:
            self.LOGGER(__name__).warning(a)
            self.LOGGER(__name__).info(
                "Bot Berhenti."
            )
            sys.exit()

app = Bot()

class User(Client):
    def __init__(self):
        super().__init__(
            name="bot",
            api_hash=API_HASH,
            api_id=API_ID,
            workers=BOT_WORKERS,
            session_string=SESSION,
            plugins=dict(root="Confess/modules"),
            in_memory=True,
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        usr_bot_me = self.me
        self.LOGGER(__name__).info(
            f"@{usr_bot_me.username} based on Pyrogram v{__version__} "
        )

bot = User()
