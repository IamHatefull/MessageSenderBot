from aiogram import Bot
from aiogram.types import Message
import json


async def get_start(message, bot):
    await bot.send_message(message.from_user.id, f'Hello {message.from_user.first_name}')
    #await message.answer(f'Hello {message.from_user.first_name} its an answer')
    #await message.reply(f'Hello {message.from_user.first_name} it is a reply')

async def get_photo(message: Message, bot: Bot):
    await message.answer(f'Ill save the image you send')
    file = await bot.get_file(message.photo[-1].file_id)
    await bot.download_file(file.file_path, 'photo.jpg')

async def get_hello(message: Message, bot: Bot):
    await message.answer(f'Hello you too!')
    #json_str = json.dumps(message.dict(), default=str)
    #print(json_str)