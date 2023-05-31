from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from core.utils.statesform import StepsForm

async def get_form(message: Message, state: FSMContext):
    await message.answer(f"{message.from_user.first_name}, let's fill a quiz. Enter your name:")
    await state.set_state(StepsForm.GET_NAME)

# State function that expect your name
async def get_name(message: Message):
    await message.answer(f'Your first name:\r\n{message.text}\r\nYour last name')