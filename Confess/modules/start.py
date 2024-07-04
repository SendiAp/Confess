import asyncio
import os

from pyrogram import *
from pyromod import listen
from pyrogram.types import *
from pyrogram.errors import FloodWait

from Confess.helper.db import *
from Confess.config import *
from Confess.tools import *
from Confess import *

from .buttons import *

CTYPE = enums.ChatType

@Bot.on_message(filters.command("start"))
@broadcast
async def start(client : Bot, message : Message):
    bot = await app.get_me()
    username = bot.username
    user = message.from_user.mention
    chat_type = message.chat.type
    if chat_type == CTYPE.PRIVATE:
        try:
            await message.reply(text=START_TEXT.format(user, username), reply_markup=START_BUTTONS)
        except FloodWait as e:
            await asyncio.sleep(e.value)
            await message.reply(text=START_TEXT.format(user, username), reply_markup=START_BUTTONS)

@app.on_callback_query(filters.regex("close"))	
async def close(client: Bot, query: CallbackQuery):
    await query.message.delete()
