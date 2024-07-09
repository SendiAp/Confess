import json
from Confess.config import *
from Confess.helper.db import *
from pyrogram.types import Message

BALANCE = 2

def get_arg(message: Message):
    msg = message.text
    msg = msg.replace(" ", "", 1) if msg[1] == " " else msg
    split = msg[1:].replace("\n", " \n").split(" ")
    if " ".join(split[1:]).strip() == "":
        return ""
    return " ".join(split[1:])

async def addlimit(user_id, limit):
    data = json.load(open('users.json', 'r'))
    user = str(user_id)
    
    if user not in data['limit']:
        data['limit'][user] = 0

    json.dump(data, open('users.json', 'w'))
    data['limit'][user] += int(limit)
    json.dump(data, open('users.json', 'w'))

def broadcast(func):
    async def wrapper(client, message):
        user_id = message.from_user.id
        broadcast = await get_gcast()
        if user_id not in broadcast:
            await add_gcast(user_id)
            await addlimit(user_id, BALANCE)
        await func(client, message)
    return wrapper

def addbl(func):
    async def wrapper(client, message):
        blacklist = await get_blacklist()
        user_id = message.from_user.id
        if user_id in blacklist:
            return await message.reply(f"❌ {message.from_user.first_name} sudah di daftar blacklist.")
        await func(client, message)
    return wrapper

def delbl(func):
    async def wrapper(client, message):
        blacklist = await get_blacklist()
        user_id = message.from_user.id
        if user_id not in blacklist:
            return await message.reply(f"❌ {message.from_user.first_name} tidak di daftar blacklist.")
        await func(client, message)
    return wrapper
    
        
