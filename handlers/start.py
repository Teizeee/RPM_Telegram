from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from state.aStates import RegisterState 

async def get_start(message: Message, state: FSMContext):
    await state.set_state(RegisterState.register_name)
    await message.answer(text="Введите ваше имя.")