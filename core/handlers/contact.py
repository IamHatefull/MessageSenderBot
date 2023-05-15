from aiogram.types import Message
from aiogram import Bot

async def get_true_contact(message: Message, bot: Bot):
    await message.answer(f'You send <b>your</b> contact.')

async def get_fake_contact(message: Message, bot: Bot):
    await message.answer(f'You send <b>not your</b> contact.')