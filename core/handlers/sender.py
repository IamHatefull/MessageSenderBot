from aiogram import Message
from aiogram import Bot
from aiogram.fsm.context import FSMContext
from aiogram.filters import CommandObject
from core.utils.sender_state import Steps

# Sender handler
async def get_sender(message: Message, command: CommandObject, state: FSMContext):
    if not command.args:
        await message.answer(f'Enter /sender command and sending name')
        return
    
    await message.answer(f'')
    await state.update_data(name_camp=command.args)
    await state.set_state(Steps.get_message)

# Get message handler
async def get_message(message: Message, state: FSMContext):
    await message.answer(f'Ok, i remembered the message you want to send.\r\n'
                         f'Should i add a button?', reply_markup = None)