import asyncio
import json
import os

from pyrogram import *
from pyromod import listen
from pyrogram.types import *

from telegraph import Telegraph, exceptions, upload_file
from Confess.helper.db import *
from Confess.config import *
from Confess import *

DOWNLOAD_LOCATION = os.environ.get("DOWNLOAD_LOCATION", "./DOWNLOADS/")

CONFESS = """
**💌MENTION CONFESS**

**From:** {}
**To:** {}

__{}__

© Send Via @SendConfessBot
"""

@Bot.on_message(filters.command("send_text"))
async def send_text(client : User, message : Message):
    text = None
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
    else:
        text = message.text.split()
        if len(text) < 2:
            await message.reply_text("❌ Format Salah..!\nGunakan Format `/send_text @KangKurirConfess`")
            return
        username = text[1]
        try:
            user = await bot.get_chat(username)
        except BaseException as e:
            return await message.reply_text(f"<b>❌ Username Tidak Ditemukan.</b>")

    data = json.load(open('users.json', 'r'))
    await message.reply(f"💌 <b>Confess</b> {username}")
    message1 = await client.ask(message.chat.id, f"🤖 <b>Bot:</b> Kirimkan nama kamu, boleh dirahasiakan. (Maks 10 karakter)", filters=filters.text)
    message1 = message1.text
    line1 = len(message1)
    
    if line1 >= 10:
        amount = len(message1)
        return await message.reply(f"🤖 <b>Bot:</b> Nama terlalu panjang! Silahkan mulai dari awal {amount}/10")
        
    message2 = await client.ask(message.chat.id, f"🤖 <b>Bot:</b> Kirimkan nama {username} , bebas mau menamai dia apa. (Maks 10 karakter)", filters=filters.text)
    message2 = message2.text
    line2 = len(message2)
    
    if line2 >= 10:
        amount = len(message2)
        return await message.reply(f"🤖 <b>Bot:</b> Nama terlalu panjang! Silahkan mulai dari awal {amount}/10")
        
    message3 = await client.ask(message.chat.id, f"🤖 <b>Bot:</b> Silahkan tuliskan pesannya, (Minimal 20 Karakter)", filters=filters.text)
    message3 = message3.text
    line3 = len(message3)
    
    if 5 >= line3:
        amount = len(message3)
        return await message.reply(f"🤖 <b>Bot:</b> Pesan terlalu pendek! Silahkan mulai dari awal {amount}/5")

    if user not in data['limit']:
        data['limit'][user] = 0

    if data['limit'][user] >= int(1):
        data['limit'][user] -= int(1)
        await bot.send_message(user.id, CONFESS.format(message1, message2, message3))
        await message.reply(f"<b>💌 [Berhasil Mengrim Confess..!](tg://openmessage?user_id={user_id})")
        json.dump(data, open('users.json', 'w'))
    else:
        await message.reply(f"❌ Gagal, Limit {message.from_user.first_name} tidak mencukupi...!")

@Bot.on_message(filters.command("send_photo"))
async def send_photo(client : User, message : Message):
    text = None
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
    else:
        text = message.text.split()
        if len(text) < 2:
            await message.reply_text("❌ Format Salah..!\nGunakan Format `/send_text @KangKurirConfess`")
            return
        username = text[1]
        try:
            user = await bot.get_chat(username)
        except BaseException as e:
            return await message.reply_text(f"<b>❌ Username Tidak Ditemukan.</b>")

    data = json.load(open('users.json', 'r'))
    await message.reply(f"💌 <b>Confess</b> {username}")

    message = await client.ask(message.chat.id, f"🤖 <b>Bot:</b> Kirimkan foto nya maks 5mb (jangan mengandung pornografi)", filters=filters.media)
    medianame = DOWNLOAD_LOCATION + str(message.from_user.id)
    await app.download_media(message=message, file_name=medianame)
    link = upload_file(medianame)
    generated_link = "https://telegra.ph" + "".join(link)

    message1 = await client.ask(message.chat.id, f"🤖 <b>Bot:</b> Kirimkan nama kamu, boleh dirahasiakan. (Maks 10 karakter)", filters=filters.text)
    message1 = message1.text
    line1 = len(message1)
    
    if line1 >= 10:
        amount = len(message1)
        return await message.reply(f"🤖 <b>Bot:</b> Nama terlalu panjang! Silahkan mulai dari awal {amount}/10")
        
    message2 = await client.ask(message.chat.id, f"🤖 <b>Bot:</b> Kirimkan nama {username} , bebas mau menamai dia apa. (Maks 10 karakter)", filters=filters.text)
    message2 = message2.text
    line2 = len(message2)
    
    if line2 >= 10:
        amount = len(message2)
        return await message.reply(f"🤖 <b>Bot:</b> Nama terlalu panjang! Silahkan mulai dari awal {amount}/10")
        
    message3 = await client.ask(message.chat.id, f"🤖 <b>Bot:</b> Silahkan tuliskan pesannya, (Minimal 20 Karakter)", filters=filters.text)
    message3 = message3.text
    line3 = len(message3)
    
    if 5 >= line3:
        amount = len(message3)
        return await message.reply(f"🤖 <b>Bot:</b> Pesan terlalu pendek! Silahkan mulai dari awal {amount}/5")

    send = str(message.from_user.id)
    if send not in data['limit']:
        data['limit'][send] = 0

    if data['limit'][send] >= int(1):
        data['limit'][send] -= int(1)
        await bot.send_photo(user.id, generated_link, CONFESS.format(message1, message2, message3))
        await message.reply(f"<b>💌 [Berhasil Mengrim Confess..!](tg://openmessage?user_id={user_id})")
        json.dump(data, open('users.json', 'w'))
    else:
        await message.reply(f"❌ Gagal, Limit {message.from_user.first_name} tidak mencukupi...!")
        
@Bot.on_message(filters.command("addlimit"))
async def addlimit(client, message):
    try:
        user_id = int(message.text.split()[1])
        limit = int(message.text.split()[2])
    except (IndexError, ValueError):
        await message.reply("❌ Gunakan Format /addlimit (user_id) - (limit)")
        return

    data = json.load(open('users.json', 'r'))
    user = str(user_id)
    
    if user not in data['limit']:
        data['limit'][user] = 0

    json.dump(data, open('users.json', 'w'))
    data['limit'][user] += int(limit)
    json.dump(data, open('users.json', 'w'))
    await message.reply(f"✅ Berhasil Mengirim Limit, Sebesar {limit}")
