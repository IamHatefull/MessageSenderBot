from aiogram import Bot
from aiogram.types import Message
import json

from core.keyboards.reply import reply_keyboard, loc_tel_poll_keyboard, get_reply_keyboard
from core.keyboards.inline import select_macbook
from core.utils.dbconnect import Request

async def get_start(message: Message, bot: Bot, request: Request):
    await request.add_data(message.from_user.id, message.from_user.first_name)

    #await bot.send_message(message.from_user.id, f'Hello {message.from_user.first_name}')
    #await message.answer(f'Hello {message.from_user.first_name} ', reply_markup= loc_tel_poll_keyboard)
    #await message.answer(f'Hello {message.from_user.first_name} ', reply_markup= reply_keyboard)
    #await message.reply(f'Hello {message.from_user.first_name} it is a reply')

# Handler to show keyboard
async def show_keyboard(message, bot):
    await message.answer('Your keyboard', reply_markup= get_reply_keyboard)

async def get_location(message: Message,bot: Bot):
    await message.answer(f'you send your location!\r\a'
                         f'{message.location.latitude}\r\n{message.location.longtitude}')

async def get_inline(message: Message,bot: Bot):
    await message.answer('Your inline keyboard', reply_markup= select_macbook)


async def get_photo(message: Message, bot: Bot):
    await message.answer(f'Ill save the image you send')
    file = await bot.get_file(message.photo[-1].file_id)
    await bot.download_file(file.file_path, 'photo.jpg')

async def get_hello(message: Message, bot: Bot):
    await message.answer(f'Hello you too!')
    #json_str = json.dumps(message.dict(), default=str)
    #print(json_str)