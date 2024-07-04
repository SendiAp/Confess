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
            InlineKeyboardButton("Groups Support", url=f"t.me/KetikaOtakPerluInspirasi1"),
        ],
    ]
)

BACK_BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("🔙Kembali", callback_data="mulai")
        ]
    ]
)
