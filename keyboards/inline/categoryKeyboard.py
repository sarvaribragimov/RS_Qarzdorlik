from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

categoryMenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="qarz olish", callback_data="getdebt"),
            InlineKeyboardButton(text="qarz berish", callback_data="givedebt"),
        ],
        [
            InlineKeyboardButton(text="qidirish", switch_inline_query_current_chat=""),
            InlineKeyboardButton(text="ulashish",switch_inline_query="chotki"),
            InlineKeyboardButton(text="bosh sahifa", callback_data="homepage"),
        ],
    ]
)