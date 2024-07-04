from Confess.config import *

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
            InlineKeyboardButton("❓Bantuan", callback_data="help"),
            InlineKeyboardButton("🛒Shop", callback_data="shop"),
        ],
        [
            InlineKeyboardButton("Groups Support", url=f"t.me{FORCE_SUB_GROUP}"),
        ],
    ]
)
