from aiogram.types import  CallbackQuery
from keyboards.default.contact_button import phonekeyboard
from loader import dp
import random
from aiogram import  types

import pdb
@dp.callback_query_handler(text="mycontact")
async def show_contact_keys(call: CallbackQuery):
    await call.message.answer(text="Kontakt yuboring:", reply_markup=phonekeyboard)

def generate_password(length=8):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    password = "".join(random.choice(characters) for _ in range(length))
    return password

import requests

@dp.message_handler(content_types='contact')
async def get_contact(message: types.Message):
    contact = message.contact
    password = generate_password(8)

    # APIga tekshirish uchun GET so'rovini yuboring
    api_url_get = "https://api.dev.realsoft.academy/api/get_tg_info"
    data_to_check = {"phone": contact.phone_number}
    res = requests.get(api_url_get, json=data_to_check)



    if res.status_code == 200:
        response_data = res.json()
        print(f'response_data===={response_data}')
        print(f'res===={res}')
        phone_exists = response_data.get("phone_exists")
        print(f'phone_exists==={phone_exists}')
        if phone_exists:
            await message.answer("Ushbu telefon raqami allaqachon mavjud.")
        else:
            # print(f"response data get exist=={response_data.get.phone_exists}")
            print(f'response_data====sddvs={response_data}')
            api_url_post = "https://api.dev.realsoft.academy/api/post_tg_add"
            b = contact.phone_number,
            c = str(b[3:]),
            print(c)
            data_to_send = {
                "username": 'user' + str(b[3:]),
                "fullname": contact.full_name,
                'telegram_id': message.from_user.id,
                'telegram_username': message.from_user.username,
                "phone": contact.phone_number,
                "password": password,


            }
            response = requests.post(api_url_post, json=data_to_send)
            print(f"response check {response}")

            if response.status_code == 200:
                data = response.json()
                await message.answer("Ma'lumotlar muvaffaqiyatli saqlandi")
                fullname = data.get("fullname")
                print(f'Fullname: {fullname}')
            else:
                error_message = "Ma'lumotlarni saqlashda xatolik yuz berdi. Xatolik kod: " + str(response.status_code)
                await message.answer(error_message)
    else:
        await message.answer("Xatolik yuz berdi. API bilan bog'lanishda xatolik.")



# @dp.message_handler(content_types='contact')
# async def get_contact(message: types.Message):
#     contact = message.contact
#     password = generate_password(8)
#
#     await message.answer(f"Rahmat, <b>{md.quote_html(contact.full_name)}</b>.\n"
#                          f"Sizning {contact.phone_number} raqamingizni qabul qildik.\n"
#                          f"Sizning parolingiz: <code>{password}</code>\n"
#                          f"Adminmiz siz bilan bog'lanadi.",
#                          parse_mode=ParseMode.HTML,
#                          reply_markup=ReplyKeyboardRemove())
#
#     api_url_get = "https://api.dev.realsoft.academy/api/get_tg_info"
#     data_to_check = {"phone": contact.phone_number,}
#     res = requests.get(api_url_get,json=data_to_check)
#     if res.status_code == 200:
#         await message.answer(" muvaffaqiyatli")
#         print(f'res==== {res}')
#     else:
#         await message.answer(" xato")
#     api_url_post = "https://api.dev.realsoft.academy/api/post_tg_add"
#     data_to_send = {
#         "fullname": contact.full_name,
#         "phone": contact.phone_number,
#         "password": password,
#     }
#     response = requests.post(api_url_post, json=data_to_send)
#
#     if response.status_code == 200:
#         data = response.json()  # JSON ma'lumotlarini o'qish
#         print(f'  data malumot {data}')
#         await message.answer("Ma'lumotlar muvaffaqiyatli saqlandi")
#         fullname = data.get("fullname")
#         # fullname = data.data.get("id")
#         print(f'fulllnamed {fullname}')
#
#     else:
#         error_message = "Ma'lumotlarni saqlashda xatolik yuz berdi. Xatolik kod: " + str(response.status_code)
#         await message.answer(error_message)
#
#     # await state.finish()
#
#
