from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

phonekeyboard = ReplyKeyboardMarkup(resize_keyboard=True,
                               keyboard=[
                                   [
                                       KeyboardButton(text="📱 telefon raqamni yuborish",
                                                      request_contact=True)
                                   ]
                               ])