import asyncio
import os

from pyrogram import *
from pyromod import listen
from pyrogram.types import *
from pyrogram.enums import ParseMode

from Confess.config import *
from Confess import *

CLOSE = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("Abaikan Pesan ini", callback_data="close")
        ]
    ]
)

CONFESS = """
**💌ADA MENFESS NIH**

**From:** {}
**To:** {}

__{}__

© Sent Via @SendConfessBot
"""

START_TEXT = """
Halo {} , Saya dapat mengirim pesan menfess ke pengguna lain💌

Gunakan Perintah:
/send_text (username) pastikan username terdaftar di telegram

👉 ini kurir saya @KangKurirMenfess
Jangan lupa dishare ketemanmu🤜
"""

ATTENTION = """
<b>⛔ BACA PENTING</b>

Karena @KangKurirMenfess masih menggunakan akun pribadi Mimin, mohon untuk minta bantuan untuk mendonasikan nokos telegram yang ber ID 1 atau 2 atau 3 atau 4 atau 5 (salah satu)
(hanya butuh satu akun saja)

cek /id (pastikan Awalan id nya 1 / 2 / 3 / 4 / 5)

Pesan ini akan hilang jika pengguna lain sudah mendonasikan nya, silahkan hubungi @pikyus7 jika ingin menyumbangkan akunnya.
"""

@Bot.on_message(filters.command("start") & filters.private)
async def start(client : User, message : Message):
    name = message.from_user.first_name
    await message.reply(START_TEXT.format(name))
    await message.reply(ATTENTION, reply_markup=CLOSE)

@app.on_callback_query(filters.regex("close"))	
async def close(client: Bot, query: CallbackQuery):
    await query.message.delete()

@Bot.on_message(filters.command("id") & filters.private)
async def id(client : User, message : Message):
    await message.reply(f"Your ID {message.from_user.id}")
    
@Bot.on_message(filters.command("send_text"))
async def send_text(client : User, message : Message):
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
        except BaseException as e:
            return await message.reply_text(f"`{e}`\n\nusername tidak di temukan.")

    await message.reply(f"🤜 Target Ditemukan {username}")
    message1 = await client.ask(message.chat.id, f"🤖 <b>Bot:</b> Kirimkan nama kamu, boleh dirahasiakan. (Min 5-10 karakter)", filters=filters.text)
    message1 = message1.text
    line1 = len(message1)
    
    if line1 >= 10:
        amount = len(message1)
        return await message.reply(f"🤖 <b>Bot:</b> Nama terlalu panjang! Silahkan mulai dari awal {amount}/10")
        
    message2 = await client.ask(message.chat.id, f"🤖 <b>Bot:</b> Kirimkan nama {username} , bebas mau menamai dia apa. (Min 5-10 karakter)", filters=filters.text)
    message2 = message2.text
    line2 = len(message2)
    
    if line2 >= 10:
        amount = len(message2)
        return await message.reply(f"🤖 <b>Bot:</b> Nama terlalu panjang! Silahkan mulai dari awal {amount}/10")
        
    message3 = await client.ask(message.chat.id, f"🤖 <b>Bot:</b> Silahkan tuliskan pesannya, (Min 20Karakter)", filters=filters.text)
    message3 = message3.text
    line3 = len(message3)
    
    if 5 >= line3:
        amount = len(message3)
        return await message.reply(f"🤖 <b>Bot:</b> Pesan terlalu pendek! Silahkan mulai dari awal {amount}/5")
        
    try:
        await bot.send_message(user.id, CONFESS.format(message1, message2, message3))
        await message.reply(f"<b>✅ Your message has been successfully sent to</b> {username}")
    except BaseException as e:
        return await message.reply_text(f"`{e}`\n\nBuruan lapor @pikyus7")
