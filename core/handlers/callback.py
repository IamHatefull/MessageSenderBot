from aiogram import Bot
from aiogram.types import CallbackQuery

async def select_macbook(call: CallbackQuery, bot: Bot):
    model = call.data.split('_')[1]
    size = call.data.split('_')[2]
    chip = call.data.split('_')[3]
    year = call.data.split('_')[4]
    answer = f'{call.message.from_user.first_name}, you choose Apple Macbook {model} with '\
                f'{size}, on chip {chip} from {year} year.'
    await call.message.answer(answer)
    await call.answer()
