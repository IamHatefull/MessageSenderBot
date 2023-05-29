from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from core.utils.statesform import StepsForm

async def get_form(message: Message, state: FSMContext):
    await message.answer(f"{message.from_user.first_name}, let's fill a quiz. Enter your name:")
    await state.set_state(StepsForm.GET_NAME)


async def get_name(message: Message):
    pass