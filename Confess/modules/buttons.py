from Confess.config import *
from pyrogram.types import *

START_BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("➕ COMMANDS ➕", callback_data="perintah"),
        ],
        [
            InlineKeyboardButton("💰Point", callback_data="point"),
            InlineKeyboardButton("💰Topup", callback_data="topup"),
        ],
        [
            InlineKeyboardButton("🎁Bonus", callback_data="help"),
            InlineKeyboardButton("🛒Shop", callback_data="shop"),
        ],
        [
            InlineKeyboardButton("Groups Support", url=f"t.me{FORCE_SUB_GROUP}"),
        ],
    ]
)

BACK_BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("🔙Kembali", callback_data="start")
        ]
    ]
)
