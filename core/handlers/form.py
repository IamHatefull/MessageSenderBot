from aiogram.types import Message

async def get_form(message: Message):
    await message.answer(f"{message.from_user.first_name}, let's fill a quiz. Enter your name:")
    