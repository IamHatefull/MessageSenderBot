from aiogram import Message
from aiogram import Bot
from aiogram.fsm.context import FSMContext
from aiogram.filters import CommandObject


async def get_sender(message: Message, command: CommandObject, state: FSMContext):
    if not command.args:
        await message.answer(f'Enter /sender command and sending name')
        return
    
    await message.answer(f'')
    await state.update_data(name_camp=command.args)
    await state.set_state()