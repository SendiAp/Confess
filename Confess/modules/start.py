import asyncio
import os

from pyrogram import *
from pyromod import listen
from pyrogram.types import *

from Confess.config import *
from Confess import *

@Bot.on_message(filters.command("confess"))
async def confess(client : User, message : Message):
    text = None
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
    else:
        text = message.text.split()
        if len(text) < 2:
            await message.reply_text("/send_text @username\n\nNB: Pastikan username valid dan terdaftar ditelegram (jangan gunakan username bot)")
            return
        username = text[1]
        try:
            user = await bot.get_chat(username)
        except ValueError:
            user = None
        if user is None:
            await message.reply_text(f"{username} tidak di temukan.")
            return
        user_id = user.id

    message1 = await client.ask(message.chat.id, f"🤖 <b>Bot:</b> Berikan saya nama anda atau nama palsu atau bisa pake Anonymous. (5-10 karakter)", filters=filters.text)

    message2 = await client.ask(message.chat.id, f"🤖 <b>Bot:</b> Berikan saya nama target yang ingin di confess. (5-10 karakter)", filters=filters.text)

    message3 = await client.ask(message.chat.id, f"🤖 <b>Bot:</b> Berikan saya pesan untuk target. (5-500 karakter)", filters=filters.text)

    await bot.send_message(user_id, f"<b>💌 ANDA MENDAPATKAN PESAN CONFESS</b>\n\n<b>From:</b> {message1.text}\n<b>To:</b> {message2.text}\n<b>Message:</b> {message3.text}")
