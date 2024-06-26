import asyncio
import os

from pyrogram import *
from pyromod import listen
from pyrogram.types import *

from Confess.config import *
from Confess import *

@Bot.on_message(filters.command("confess"))
async def confess(client : User, message : Message):
    quantity = 1
    inp = message.text.split(None, 2)[1]
    user = await bot.get_chat(inp)
    spam_text = ' '.join(message.command[2:])
    quantity = int(quantity)

    if message.reply_to_message:
        reply_to_id = message.reply_to_message.message_id
        for _ in range(quantity):
            await message.edit("Message Sended Successfully !")
            await bot.send_message(user.id, spam_text,
                                      reply_to_messsge_id=reply_to_id)
            await asyncio.sleep(0.15)
        return

    for _ in range(quantity):
        await bot.send_message(user.id, spam_text)
        await message.edit("Message Sended Successfully !")
        await asyncio.sleep(0.15)
