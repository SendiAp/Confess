import asyncio
import os
import time
import pytz
import json

from pyrogram import *
from pyromod import listen
from pyrogram.types import *
from pyrogram.errors import FloodWait

from Confess.helper.db import *
from Confess.config import *
from Confess.helper.tools import *
from Confess import *

from .message import *
from .buttons import *

@app.on_message(filters.command("start"))
@broadcast
async def start(client : Bot, message : Message):
    chat_type = message.chat.type
    if chat_type == CTYPE.PRIVATE:
        try:
            await message.reply(text=START_TEXT, reply_markup=START_BUTTONS)
        except FloodWait as e:
            await asyncio.sleep(e.value)
            await message.reply(text=START_TEXT, reply_markup=START_BUTTONS)

@app.on_message(filters.command("help"))
async def help(client : Bot, message : Message):
    chat_type = message.chat.type
    if chat_type == CTYPE.PRIVATE:
        try:
            await message.reply(text=COMMANDS, reply_markup=BACK_BUTTONS)
        except FloodWait as e:
            await asyncio.sleep(e.value)
            await message.reply(text=COMMANDS, reply_markup=BACK_BUTTONS)

@app.on_message(filters.command("Jancok"))
async def Jancok(client : Bot, message : Message):
    await remove_gcast(message.from_user.id)
    await message.reply("berhasil")
    
@app.on_callback_query(filters.regex("mulai"))	
async def mulai(client: Bot, query: CallbackQuery):
    try:
        await query.edit_message_text(START_TEXT, reply_markup=START_BUTTONS)
    except FloodWait as e:
        await asyncio.sleep(e.value)
        await query.edit_message_text(START_TEXT, reply_markup=START_BUTTONS)

@app.on_callback_query(filters.regex("point"))	
async def point(client: Bot, query: CallbackQuery):
    data = json.load(open('users.json', 'r'))
    user = str(query.from_user.id)
    name = query.from_user.first_name
    
    if user not in data['limit']:
        data['limit'][user] = 0

    json.dump(data, open('users.json', 'w'))
    point = data['limit'][user]
    await query.answer(f"💰Point {name}: {point}", cache_time=0, show_alert=True)

@app.on_callback_query(filters.regex("perintah"))	
async def perintah(client: Bot, query: CallbackQuery):
    await query.edit_message_text(COMMANDS, reply_markup=BACK_BUTTONS)
