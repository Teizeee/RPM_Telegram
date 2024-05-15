from aiogram.fsm.state import StatesGroup, State

class RegisterState(StatesGroup):
    register_name=State()
    select_name=State()
    register_spec=State()
    select_spec=State()
