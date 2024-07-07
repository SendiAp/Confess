from Confess.config import *
from pyrogram.types import *

START_BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("➕ COMMANDS ➕", callback_data="perintah"),
        ],
        [
            InlineKeyboardButton("💰Point", callback_data="point"),
            InlineKeyboardButton("💳Deposit", callback_data="topup"),
        ],
        [
            InlineKeyboardButton("Rules Confess", url=f"http://t.me/{BOT_USERNAME}?start=rules"),
        ],
    ]
)

PRICE_BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("Beli 💰Point", url=f"tg://openmessage?user_id=6847847442"),
        ],
        [
            InlineKeyboardButton("🔙Kembali", callback_data="mulai"),
        ]
    ]
)

BACK_BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("🔙Kembali", callback_data="mulai")
        ]
    ]
)
