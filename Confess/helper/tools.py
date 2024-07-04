import json
from pyrogram.types import Message

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
