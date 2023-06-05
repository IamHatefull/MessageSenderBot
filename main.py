
import asyncio
import logging
import asyncpg

from aiogram import Bot, Dispatcher
from aiogram.types import Message, ContentType
from aiogram.filters import  Command
from aiogram import F

# Import files from project directory
from core.settings import settings
from core.handlers.basic import get_start, get_photo, get_hello, get_location
from core.handlers.basic import show_keyboard, get_inline
from core.handlers.contact import get_fake_contact, get_true_contact
from core.handlers.callback import select_macbook
from core.handlers import form
from core.filters.iscontact import IsTrueContact
from core.utils.commands import set_commands
from core.utils.statesform import StepsForm
from core.middlewares.dbmiddleware import DBSession


# Small function to show that bot is running
async def start_bot(bot: Bot):
    await set_commands(bot)
    await bot.send_message( settings.bots.admin_id, text="Bot is running")

# Small function to show that bot is stopped
async def stop_bot(bot:Bot):
    await bot.send_message( settings.bots.admin_id, text="Bot is stopped")

async def start():
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s.%(funcName)s(%(lineno)d) - %(message)s)"
                                
                        )
    
    # Create a connection to the bot through token given by BotFather
    bot = Bot(token=settings.bots.bot_token, parse_mode='HTML')
    pool_connect = await asyncpg.create_pool(user="postgres", password='qwerty', database='users',
                                             host='127.0.0.1', port=5432, command_timeout=60)

    # Dispatcher object
    dp = Dispatcher()
    
    # Registration of all functions
    dp.update.middleware.register(DBSession(pool_connect))
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
    dp.callback_query.register(select_macbook, F.data.startswith('apple_'))
    #dp.message.register(form.get_form, StepsForm.GET_NAME)
    dp.message.register(form.get_name, Command(commands='form'))
    dp.message.register(get_start, Command(commands=['start', 'run']))
    dp.message.register(show_keyboard, Command(commands=['show']))
    dp.message.register(get_inline, Command(commands='inline'))
    dp.message.register(get_location, F.location)
    dp.message.register(get_true_contact, F.contact, IsTrueContact())
    dp.message.register(get_fake_contact, F.contact)
    dp.message.register(get_photo, F.photo)
    dp.message.register(get_hello, F.text == 'Hello')

    try: 
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(start())

