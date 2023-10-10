from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import Message
from loader import dp
from states.personalData import PersonalData
import requests


@dp.message_handler(Command("anketa"), state=None)
async def enter_test(message: types.Message):
    await message.answer("to'liq ismingizni kiriting")
    await PersonalData.fullname.set()

@dp.message_handler(state=PersonalData.fullname)
async def answer_fullname(message: types.Message, state:FSMContext):
    fullname = message.text

    await state.update_data(
        {"fullname": fullname }
    )
    await message.answer('Emailingizni kiriting')
    await PersonalData.next()

@dp.message_handler(state=PersonalData.email)
async def answer_email(message: types.Message, state: FSMContext):
    email = message.text

    await state.update_data(
        {"email": email}
    )
    await message.answer('telefon raqam kiriting')
    await PersonalData.next()


# @dp.message_handler(state=PersonalData.phonenum)
# async def answer_phone(message: types.Message, state: FSMContext):
#     phone = message.text
#
#     await state.update_data(
#         {"phone": phone}
#     )
#
#     data = await  state.get_data()
#     name = data.get('name')
#     email = data.get('email')
#     phone = data.get('phone')
#
#     msg = "quyidagi malumotlar qabul qilindi:\n"
#     msg += f"ismingiz - {name}\n"
#     msg += f"ismingiz - {email}\n"
#     msg += f"ismingiz - {phone}\n"
#
#     await message.answer(msg)


@dp.message_handler(lambda message: not message.text.lower().startswith("http"), state=PersonalData.phonenum)
async def process_phonenum(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['phonenum'] = message.text

    api_url = "https://api.dev.realsoft.academy/api/post_tg_add"
    data_to_send = {
        "fullname": data['fullname'],
        "email": data['email'],
        "phone": data['phonenum'],
    }
    response = requests.post(api_url, json=data_to_send)
    if response.status_code == 200:
        await message.answer("Ma'lumotlar muvaffaqiyatli saqlandi")
    else:
        await message.answer("Ma'lumotlarni saqlashda xatolik yuz berdi")


    await state.finish()
