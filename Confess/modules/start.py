import asyncio
import os

from pyrogram import *
from pyromod import listen
from pyrogram.types import *
from pyrogram.enums import ParseMode

from Confess.config import *
from Confess import *

FORCESUB = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("Bergabung Ke Groups", url=f"t.me/PTSMProject"),
        ],
        [
            InlineKeyboardButton("Coba Lagi", url=f"t.me/KetikaOtakPerluInspirasi1"),
        ],
    ]
)

CONFESS = """
<b>💌ANDA MENDAPATKAN PESAN MENFESS</b>

{}

© @PTSMProject
"""

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

    message = await client.ask(message.chat.id, f"🤖 <b>Bot:</b> Silahkan tuliskan pesannya, Min 20Karakter", filters=filters.text)

    try:
        await bot.send_message(user_id, CONFESS.format(('> message'))
    
