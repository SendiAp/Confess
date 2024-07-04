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

@Bot.on_message(filters.command("start") & filters.private)
@broadcast
async def start(client : Bot, message : Message):
    user = message.from_user.mention
    await message.reply(text=START_TEXT.format(user), reply_markup=START_BUTTONS)

@app.on_callback_query(filters.regex("mulai"))	
async def mulai(client: Bot, query: CallbackQuery):
    await query.edit_message_text(START_TEXT, reply_markup=START_BUTTONS)

bonus = {}

@app.on_callback_query(filters.regex("bonus"))
async def bonus(client: bot, query: CallbackQuery):
    user_id = query.from_user.id
    user = str(user_id)
    name = query.from_user.first_name
    cur_time = int((time.time()))
    Daily_bonus = 5
    data = json.load(open('users.json', 'r'))

    if user not in data['limit']:
        data['limit'][user] = 0

    json.dump(data, open('users.json', 'w'))
    if (user_id not in bonus.keys()) or (cur_time - bonus[user_id] > 60*60*24):
        data['limit'][(user)] += int(Daily_bonus)
        await query.answer(f"{query.from_user.first_name} Berhasil Mendapatkan +{Daily_bonus}💰Point", cache_time=0, show_alert=True)
        bonus[user_id] = cur_time
        json.dump(data, open('users.json', 'w'))
    else:
        await query.answer(f"❌ {name} Hanya dapat mengklaim bonus setiap 24 jam sekali.", cache_time=0, show_alert=True)


@app.on_callback_query(filters.regex("point"))	
async def point(client: Bot, query: CallbackQuery):
    data = json.load(open('users.json', 'r'))
    user = str(query.from_user.id)
    name = query.from_user.first_name
    
    if user not in data['limit']:
        data['limit'][user] = 0

    json.dump(data, open('users.json', 'w'))
    point = data['limit'][user]
    await query.answer(f"💰Point {name}: 💰{point}")

@app.on_callback_query(filters.regex("perintah"))	
async def perintah(client: Bot, query: CallbackQuery):
    await query.edit_message_text(COMMANDS, reply_markup=BACK_BUTTONS)
