
import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.types import Message, ContentType
from settings import settings
from handlers.basic import get_start, get_photo, get_hello
from aiogram.filters import  Command
from aiogram import F


async def start_bot(bot: Bot):
    await bot.send_message( settings.bots.admin_id, text="Bot is running")

async def stop_bot(bot:Bot):
    await bot.send_message( settings.bots.admin_id, text="Bot is stopped")


'''
async def get_photo(message: Message, bot: Bot):
    await message.answer(f'Ill save the image you send')
    file = await bot.get_file(message.photo[-1].file_id)
    await bot.download_file(file.file_path, 'photo.jpg')
'''

async def start():
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s.%(funcName)s(%(lineno)d) - %(message)s)"
                                
                        )
    bot = Bot(token=settings.bots.bot_token)

    dp = Dispatcher()

    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
    dp.message.register(get_start, Command(commands=['start', 'run']))
    dp.message.register(get_photo, F.photo)
    dp.message.register(get_hello, F.text == 'Hello')

    try: 
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(start())

