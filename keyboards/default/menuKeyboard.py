from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
from loader import dp
menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Registration"),
            KeyboardButton(text="🔐login"),

        ],
    ],
    resize_keyboard=True
)



