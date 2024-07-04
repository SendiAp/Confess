import asyncio
import os

from pyrogram import *
from pyromod import listen
from pyrogram.types import *

from Confess.helper.db import *
from Confess.config import *
from Confess import *

CLOSE = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("Abaikan Pesan ini", callback_data="close")
        ]
    ]
)
    
def get_arg(message: Message):
    msg = message.text
    msg = msg.replace(" ", "", 1) if msg[1] == " " else msg
    split = msg[1:].replace("\n", " \n").split(" ")
    if " ".join(split[1:]).strip() == "":
        return ""
    return " ".join(split[1:])

def broadcast(func):
    async def wrapper(client, message):
        user_id = message.from_user.id
        broadcast = await get_gcast()
        if user_id not in broadcast:
            await add_gcast(user_id)
        await func(client, message)
    return wrapper

START_TEXT = """
👋Hai {}!
@GroupsHelpBot Adalah <b>Bot yang akan membantu</b> Kalian mengirim menfess crush mu langsung.

<b>👉Kurir Saya</b> @KangKurirMenfess Dia akan mengantarkan pesan menfess mu.

<b>❓ APA SAJA PERINTAHNYA ❓</b>
Tekan /help untuk melihat semua daftar perintah dan cara kerjanya.

[📃Rules Confess](t.me/PTSMProject)
"""

ATTENTION = """
<b>⛔ BACA PENTING</b>

Karena @KangKurirMenfess masih menggunakan akun pribadi Mimin, mohon untuk minta bantuan untuk mendonasikan nokos telegram yang ber ID 1 atau 2 atau 3 atau 4 atau 5 (salah satu)
(hanya butuh satu akun saja)

cek /id (pastikan Awalan id nya 1 / 2 / 3 / 4 / 5)

Pesan ini akan hilang jika pengguna lain sudah mendonasikan nya, silahkan hubungi @pikyus7 jika ingin menyumbangkan akunnya.
"""

@Bot.on_message(filters.command("start") & filters.private)
@broadcast
async def start(client : User, message : Message):
    name = message.from_user.first_name
    await message.reply(START_TEXT.format(name))
    
@app.on_callback_query(filters.regex("close"))	
async def close(client: Bot, query: CallbackQuery):
    await query.message.delete()

@Bot.on_message(filters.command("id") & filters.private)
async def id(client : User, message : Message):
    await message.reply(f"Your ID `{message.from_user.id}`")
