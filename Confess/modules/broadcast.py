import asyncio
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

@Bot.on_message(filters.command("gucast") & filters.user(OWNER_ID))
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

@Bot.on_message(filters.command("stats")  & filters.user(OWNER_ID))
async def stats(client : Bot, message : Message):
    ss = await get_gcast()
    user = len(ss)
    await message.reply(MSG.format(user))
  
