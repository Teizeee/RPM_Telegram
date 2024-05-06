from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from state.aStates import RegisterState
from keyboards.keyboard_reg import IlKeyBoard, SpecKeyBoard
from database.db import data
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
                await message.answer(text=f"Тебя зовут, {name}?", reply_markup=IlKeyBoard())
                await state.set_state(RegisterState.select_name)
    else: 
        await message.answer(text="Стикеры и прочее не могут быть вашим именем.")
        await state.set_state(RegisterState.register_name)

async def select_name(call: CallbackQuery, state: FSMContext):
    await call.answer()
    if call.data=="Да":
        data[0]=name
        await call.message.edit_reply_markup(reply_markup=None)
        await call.message.answer("На кого ты хочешь поступить?",reply_markup=SpecKeyBoard())
        await state.set_state(RegisterState.register_spec)

    elif call.data=="Нет":
        await call.message.edit_reply_markup(reply_markup=None)
        await call.message.answer("Введите еще раз свое имя.")
        await state.set_state(RegisterState.register_name)
