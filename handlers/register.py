from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from state.aStates import RegisterState
from keyboards.keyboard_reg import SpecKeyBoard
from basemodel.db import data
import emoji

async def get_start(message: Message, state: FSMContext):
    await state.set_state(RegisterState.register_name)
    await message.answer(text="Введите ваше имя.")
    
async def register_name(message: Message, state: FSMContext):
    global name
    if message.text:
            if emoji.emoji_count(message.text)>0:
                await message.answer(text="Ваше имя не может содержать эмодзи.")
                await state.set_state(RegisterState.register_name)
            else:
                name=message.text
                data[0]=name
                await message.answer("На кого ты хочешь поступить?",reply_markup=SpecKeyBoard())
                await state.set_state(RegisterState.register_spec)
    else: 
        await message.answer(text="Стикеры и прочее не могут быть вашим именем.")
        await state.set_state(RegisterState.register_name)
