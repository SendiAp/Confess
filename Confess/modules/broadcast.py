import asyncio
import json
import os

from pyrogram import *
from pyromod import listen
from pyrogram.types import *

from Confess.helper.db import *
from Confess.config import *
from Confess import *

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

@app.on_message(filters.command("gucast") & filters.user(OWNER_ID))
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

@app.on_message(filters.command("addlimit"))
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

    users = await client.get_users(user_id)
    name = users.first_name
    json.dump(data, open('users.json', 'w'))
    data['limit'][user] += int(limit)
    json.dump(data, open('users.json', 'w'))
    await message.reply(f"<b>💳Deposit</b> Sebesar <b>+{limit}💰Point</b> Berhasil masuk akun {name} ..!")
    await app.send_message(users.id, f"<b>💳Deposit</b> Sebesar <b>+{limit}💰Point</b> Berhasil masuk akunmu ..!")
    
MSG = """
<b>📊 Statistik</b>

<b>Jumlah Users:</b> {}
"""

@app.on_message(filters.command("stats")  & filters.user(OWNER_ID))
async def stats(client : Bot, message : Message):
    ss = await get_gcast()
    user = len(ss)
    await message.reply(MSG.format(user))
  
