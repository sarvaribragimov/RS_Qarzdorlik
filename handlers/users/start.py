import logging

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default.menuKeyboard import menu
from keyboards.default.registerkeyboard import menulogin
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    logging.info(message)
    logging.info(f' ismi ={message.from_user.full_name}')
    logging.info(f"username = {message.from_user.username}")
    await message.answer(f"Salom,  {message.from_user.full_name} Qarzdorlik botiga xush kelibsiz \n"
                         f"Korxona Realsoft \n"
                         f"👇Kerakli bo'limni tanlang!",reply_markup=menu)



