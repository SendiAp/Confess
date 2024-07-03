from pyrogram.types import *
from typing import Dict, List, Union
from motor.motor_asyncio import AsyncIOMotorClient

from Confess.config import *

mongo_client = AsyncIOMotorClient(MONGO_DB_URL)
db = mongo_client[DB_NAME]

gcastdb = db['GCAST']
blacklistdb = db['BLACKLIST']

#BROADCAST_USER
async def get_gcast() -> list:
    gcast = await gcastdb.find_one({"gcast_id": "gcast_id"})
    if not gcast:
        return []
    return gcast["gcast"]

async def add_gcast(user_id: int) -> bool:
    gcast = await get_gcast()
    gcast.append(user_id)
    await gcastdb.update_one(
        {"gcast_id": "gcast_id"}, {"$set": {"gcast": gcast}}, upsert=True
    )
    return True

async def remove_gcast(user_id: int) -> bool:
    gcast = await get_gcast()
    gcast.remove(user_id)
    await gcastdb.update_one(
        {"gcast_id": "gcast_id"}, {"$set": {"gcast": gcast}}, upsert=True
    )
    return True
    
async def get_blacklist() -> list:
    blacklist = await blacklistdb.find_one({"blacklist_id": "blacklist_id"})
    if not blacklist:
        return []
    return blacklist["blacklist"]

async def add_blacklist(user_id: int) -> bool:
    blacklist = await get_blacklist()
    blacklist.append(user_id)
    await blacklistdb.update_one(
        {"blacklist_id": "blacklist_id"}, {"$set": {"blacklist": blacklist}}, upsert=True
    )
    return True

async def remove_blacklist(user_id: int) -> bool:
    blacklist = await get_blacklist()
    blacklist.remove(user_id)
    await blacklistdb.update_one(
        {"blacklist_id": "blacklist_id"}, {"$set": {"blacklist": blacklist}}, upsert=True
    )
    return True
    
