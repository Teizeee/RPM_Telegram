from aiogram import Dispatcher, Bot
from state.aStates import RegisterState
from aiogram.filters import Command
from utils.commands import set_commands
from handlers.start import get_start
from handlers.register import register_name, select_name
from handlers.spec import speciality_kb,speciality_config
import asyncio


bot=Bot(token="6979731298:AAF5hDzrMvf-klQTArWl1I_ZAK3BKl8gjcM")
dp=Dispatcher()

dp.message.register(get_start,Command(commands="start"))
dp.message.register(register_name,RegisterState.register_name)
dp.callback_query.register(select_name,RegisterState.select_name)
dp.callback_query.register(speciality_kb,RegisterState.register_spec)
dp.callback_query.register(speciality_config,RegisterState.select_spec)

async def start():
    await set_commands(bot)
    try:
        await dp.start_polling(bot,skip_updates=True)
    finally:
        await bot.session.close()
if __name__=="__main__":
    asyncio.run(start())
