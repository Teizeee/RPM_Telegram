from aiogram.utils.keyboard import InlineKeyboardBuilder

def SpecConfKeyBoard():
    kb=InlineKeyboardBuilder()
    kb.button(text="Подтвердить",callback_data="Да")
    kb.button(text="Назад",callback_data="Нет")
    return kb.as_markup()

def SpecKeyBoard():
    kb=InlineKeyboardBuilder()
    kb.button(text="Архитектура",callback_data="Арх")
    kb.button(text="Гидрогеология (Гидрогеология и инженерная геология)", callback_data="Гид")
    kb.button(text="ИСиП (Информационные системы и программирование)", callback_data="Прог")
    kb.button(text="СиЭЗИС (Строительство и эксплуатация зданий и сооружений)", callback_data="Строит")
    kb.button(text="ЭПиУ (Электронные приборы и устрйства)", callback_data="Элек")
    kb.adjust(1)
    return kb.as_markup()