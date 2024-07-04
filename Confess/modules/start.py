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

from .message import *
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

@app.on_callback_query(filters.regex("start"))	
async def start(client: Bot, query: CallbackQuery):
    await query.edit_message_text(START_TEXT, reply_markup=START_BUTTONS)
    
@app.on_callback_query(filters.regex("point"))	
async def point(client: Bot, query: CallbackQuery):
    data = json.load(open('users.json', 'r'))
    user = str(message.from_user.id)
    name = message.from_user.first_name
    
    if user not in data['limit']:
        data['limit'][user] = 0

    json.dump(data, open('users.json', 'w'))
    point = data['limit'][user]
    await query.answer(f"💰Point {name}: 💰{point})

@app.on_callback_query(filters.regex("perintah"))	
async def perintah(client: Bot, query: CallbackQuery):
    await query.edit_message_text(COMMANDS, reply_markup=BACK_BUTTONS)
