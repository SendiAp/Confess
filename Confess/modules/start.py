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

def broadcast(func):
    async def wrapper(client, message):
        user_id = message.from_user.id
        broadcast = await get_gcast()
        limit = 10
        if user_id not in broadcast:
            await add_gcast(user_id)
            await add_limit(user_id, limit)
        await func(client, message)
    return wrapper

START_TEXT = """
👋Hai {}!
@{} Adalah <b>Bot yang akan membantu</b> Kalian mengirim menfess crush mu langsung.

<b>👉Kurir Saya</b> @KangKurirMenfess Dia akan mengantarkan pesan menfess mu.

<b>❓ APA SAJA PERINTAHNYA ❓</b>
Tekan /help untuk melihat semua daftar perintah dan cara kerjanya.

[📃Rules Confess](t.me/PTSMProject)
"""

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
