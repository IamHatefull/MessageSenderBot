from aiogram.fsm.state import StatesGroup, State

# Class for state machine
class StepsForm(StatesGroup):
    GET_NAME = State()
