from aiogram.types import Message
from aiogram import Bot

# Function will send you an answer if the contact you provided is yours
async def get_true_contact(message: Message, bot: Bot):
    await message.answer(f'You send <b>your</b> contact.')

# Function will send you an answer if the contact you provided is not yours
async def get_fake_contact(message: Message, bot: Bot):
    await message.answer(f'You send <b>not your</b> contact.')