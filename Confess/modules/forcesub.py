from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden
from pyrogram.types import *
from pyrogram import filters
from Confess.config import *
from Confess import *

FORCESUB = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("Bergabung Ke Channel", url=f"t.me/{FORCE_SUB_CHANNEL}"),
        ],
        [
            InlineKeyboardButton("Bergabung Ke Groups", url=f"t.me/{FORCE_SUB_GROUP}"),
        ],
        [
            InlineKeyboardButton("Coba Lagi", url=f"http://t.me/{BOT_USERNAME}?start=start"),
        ],
    ]
)

@app.on_message(filters.incoming & filters.private, group=-1)
async def ForceSub(client: Bot, message: Message):
    if not FORCE_SUB_CHANNEL and not FORCE_SUB_GROUP:  # Not compulsory
        return
    try:
        try:
            await client.get_chat_member(FORCE_SUB_CHANNEL, message.from_user.id)
            await client.get_chat_member(FORCE_SUB_GROUP, message.from_user.id)
        except UserNotParticipant:
            if FORCE_SUB_CHANNEL.isalpha():
                link = "https://t.me/" + FORCE_SUB_CHANNEL
            if FORCE_SUB_CHANNEL.isalpha():
                link2 = "https://t.me/" + FORCE_SUB_GROUP
            else:
                chat_info = await client.get_chat(FORCE_SUB_CHANNEL)
                link = chat_info.invite_link
                chat = await client.get_chat(FORCE_SUB_GROUP)
                link2 = chat.invite_link
            try:
                await message.reply(
                    f"<b>{message.from_user.first_name}</b> Belum bergabung dichannel/groups kami, silahkan bergabung lalu coba lagi.",
                    disable_web_page_preview=True,
                    reply_markup=FORCESUB)

                await message.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"❌ I am not an admin in one of your groups or channels.!")

