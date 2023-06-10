from aiogram import Message
from aiogram import Bot
from aiogram.fsm.context import FSMContext
from aiogram.filters import CommandObject


async def get_sender(message: Message, command: CommandObject, state: FSMContext):
    pass