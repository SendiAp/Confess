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
            InlineKeyboardButton("Abaikan Pesan ini", callback_data="close"),
        ],
        [
            InlineKeyboardButton("Abaikan Pesan ini", callback_data="close"),
        ],
    ]
)
