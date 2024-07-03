import asyncio
import os

from pyrogram import *
from pyromod import listen
from pyrogram.types import *

from Confess.helper.db import *
from Confess.config import *
from Confess import *

ADMINS = [6847847442]

CLOSE = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("Abaikan Pesan ini", callback_data="close")
        ]
    ]
)

def admins(func):
    async def wrapper(client, message):
        user_id = message.from_user.id
        if user_id not in ADMINS:
            p = await message.reply_text(f"❌ <b>Hanya Admins!</b>")
            await p.delete()
            return 
        await func(client, message)
    return wrapper
    
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
        await message.reply(ATTENTION, reply_markup=CLOSE)
    except BaseException as e:
        return await message.reply_text(f"`{e}`\n\nBuruan lapor @pikyus7")

async def send_msg(chat_id, message: Message):
    try:
        if BROADCAST_AS_COPY is False:
            await message.forward(chat_id=chat_id)
        elif BROADCAST_AS_COPY is True:
            await message.copy(chat_id=chat_id)
        return 200, None
    except FloodWait as e:
        await asyncio.sleep(int(e.value))
        return send_msg(chat_id, message)

@Bot.on_message(filters.command("gucast"))
@admins
async def SMProjectUser(client : Bot, message : Message):
    users = await get_gcast()
    msg = get_arg(message)
    if message.reply_to_message:
        msg = message.reply_to_message

    if not msg:
        await message.reply(text="**Reply atau berikan saya sebuah pesan!**")
        return
    
    out = await message.reply(text="**Memulai Broadcast...**")
    
    if not users:
        await out.edit(text="**Maaf, Broadcast Gagal Karena Belum Ada user**")
        return
    
    done = 0
    failed = 0
    for user in users:
        try:
            await send_msg(user, message=msg)
            done += 1
        except:
            failed += 1
    await out.edit(f"✅ **Berhasil Mengirim Pesan Ke {done} User.**\n❌ **Gagal Mengirim Pesan Ke {failed} User.**")

MSG = """
<b>📊 Statistik</b>

<b>Jumlah Users:</b> {}
"""

@Bot.on_message(filters.command("stats"))
@admins
async def stats(client : Bot, message : Message):
    ss = await get_gcast()
    user = len(ss)
    await message.reply(MSG.format(user))
