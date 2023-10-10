from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
from loader import dp
menulogin = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="openweb"),
            KeyboardButton(text="menu"),
        ],
        [
            KeyboardButton(text="ortga"),
            KeyboardButton(text="boshiga"),
        ],
    ],
    resize_keyboard=True
)


