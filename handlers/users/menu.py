from aiogram.dispatcher.filters import Command

from keyboards.default.contact_button import phonekeyboard
from keyboards.default.menuKeyboard import menu
from keyboards.default.registerkeyboard import menulogin
from aiogram import types
from loader import dp
from aiogram import Bot
from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    MenuButtonWebApp,
    Message,
    WebAppInfo,
)

@dp.message_handler(commands=("menue"))
async def show_menu(message:Message):
    await message.answer("registratsiyadan o'ting ",reply_markup=menu)



@dp.message_handler(text="Registration")
async def show_login(message:Message):
    await message.answer("Ro'yxatdan o'ting ",reply_markup=phonekeyboard)

@dp.message_handler(commands=("web"))
async def show_web(message:Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('d'))
    await message.answer("registratsiyadan o'ting ",reply_markup=menu)


@dp.message_handler(text="Registrations")
async def show_registration(message: Message):
    url = "https://dev.realsoft.academy/pages/s_qarz_login"
    await message.answer(f"Ro'yxatdan o'tish uchun ushbu manzilni oching:\n{url}", reply_markup=menu)

@dp.message_handler(text="boshiga")
async def show_login(message:Message):
    await message.answer("registratsiyadan o'ting ",reply_markup=menu)






@dp.message_handler(Command("menu"))
async def command_start(bot:Bot, message: Message):
    # base_url = dp["base_url"]
    await bot.set_chat_menu_button(
        menu_button=MenuButtonWebApp(
            type="web_app", text="web app open",
            web_app=WebAppInfo(url="https://google.com")
        )
    )
    await message.answer("Hi! Send me any type of message to start or just send /webview.")



@dp.message_handler(text="openweb")
async def command_webview(message: Message):
    base_url = "https://dev.realsoft.academy/pages/login_form_test.com"
    await message.answer(
        "registration",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text="Registration website", web_app=WebAppInfo(url=f"{base_url}/demo")
                    )
                ]
            ]
        ),
    )
