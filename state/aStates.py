from aiogram.fsm.state import StatesGroup, State

class RegisterState(StatesGroup):
    register_name=State()
    register_spec=State()
    select_spec=State()
