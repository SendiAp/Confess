import asyncio
from Confess import Bot, app, bot
from Confess.config import LOGGER
from pyrogram import idle


loop = asyncio.get_event_loop_policy().get_event_loop()

async def main():
    try:
        await app.start()
        app.me = await app.get_me()
        username = app.me.username
        namebot = app.me.first_name
        LOGGER("INFO").info(f"{namebot} | [ @{username} ] | 🔥 BERHASIL DIAKTIFKAN! 🔥")
    except Exception as a:
        print(a)
    LOGGER("INFO").info(f"[🔥 BOT AKTIF! 🔥]")
    await idle()


LOGGER("INFO").info("Starting Bot...")
loop.run_until_complete(main())
