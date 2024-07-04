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

PRICE_BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("Beli 💰Point", url=f"mulai"),
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
