from Confess.config import *

START_BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("➕ COMMANDS ➕", callback_data="close"),
        ],
        [
            InlineKeyboardButton("💰Point", callback_data="close"),
            InlineKeyboardButton("💰Topup", callback_data="close"),
        ],
        [
            InlineKeyboardButton("❓Bantuan", callback_data="close"),
            InlineKeyboardButton("♻️Price", callback_data="close"),
        ],
        [
            InlineKeyboardButton("Groups Support", url=f"t.me{FORCE_SUB_GROUP}"),
        ],
    ]
)
