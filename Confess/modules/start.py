import asyncio
import os

from pyrogram import *
from pyrogram.types import *

from Confess.config import *
from Confess import *

@Bot.on_message(filters.command("confess"))
async def confess(client : Bot, message : Message):
    text = None
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
    else:
        text = message.text.split()
        if len(text) < 2:
            await message.reply_text("Maaf, format yang Anda berikan salah. Mohon balas ke pengguna atau berikan username/user ID.")
            return
        username = text[1]
        try:
            user = await client.get_users(username)
        except ValueError:
            user = None
        if user is None:
            await message.reply_text(f"Maaf, pengguna {username} tidak ditemukan.")
            return
        user_id = user.id

    await bot.send_message(user_id, "Halo")
