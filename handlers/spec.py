from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from state.aStates import RegisterState 
from keyboards.keyboard_reg import SpecConfKeyBoard,SpecKeyBoard
from database.db import User,data


async def speciality_kb(call: CallbackQuery, state: FSMContext):
    global spec
    await call.answer()
    if call.data=="Арх":
        spec="Архитектор"
        await call.message.answer("Архитектор — это специалист, который участвует в проектировании и строительстве различных объектов — зданий, сооружений и территорий. "
        "Основные обязанности архитектора:\nРазработка концепции здания и интерьеров.\nВизуализация принятых архитектурных и проектных решений в виде эскизов и чертежей.\n"
        "Изготовление графических альбомов и макетов.\nСогласование проектной документации с контролирующими органами и получение необходимых разрешений.",reply_markup=SpecConfKeyBoard())
        await call.message.edit_reply_markup(reply_markup=None)
        await state.set_state(RegisterState.select_spec)

    elif call.data=="Гид":
        spec="Гидрогеолог"
        await call.message.answer("Гидрогеолог - это специалист, изучающий подземные воды, их происхождение, движение, "
        "физические и химические свойства, а также их взаимодействие с горными породами и влияние на окружающую среду. Гидрогеологи занимаются следующими основными задачами:\n"
        "Изучение водоносных горизонтов и их характеристик.\nРазведка и оценка запасов подземных вод.\nМониторинг и охрана подземных вод.\nПроектирование и эксплуатация водозаборных сооружений.\nГидрогеологическое обоснование строительных работ.",reply_markup= SpecConfKeyBoard())
        await call.message.edit_reply_markup(reply_markup=None)
        await state.set_state(RegisterState.select_spec)
        
    elif call.data=="Прог":
        spec="Программист"
        await call.message.answer("Программист - это специалист, занимающийся разработкой и созданием компьютерных программ и программного обеспечения. "
        "Вот основные обязанности и сферы деятельности программистов:\nНаписание кода на различных языках программирования.\nПроектирование и разработка архитектуры программного обеспечения.\n"
        "Анализ требований к программному обеспечению и их реализация в коде.\nТестирование и отладка программного кода для выявления и устранения ошибок.\nОптимизация производительности и эффективности работы программ.",reply_markup= SpecConfKeyBoard())
        await call.message.edit_reply_markup(reply_markup=None)
        await state.set_state(RegisterState.select_spec)
                
    elif call.data=="Строит":
        spec="Строитель"
        await call.message.answer("Строитель - это специалист, занимающийся возведением зданий, сооружений и других строительных объектов. Профессия строителя включает в себя следующие основные направления деятельности:\n"
        "Подготовительные работы.\nЗемляные работы.\nСтроительно-монтажные работы.\nСпециализированные работы.\nКонтроль качества и соблюдение технологий.",reply_markup= SpecConfKeyBoard())
        await call.message.edit_reply_markup(reply_markup=None)
        await state.set_state(RegisterState.select_spec)
                        
    elif call.data=="Элек":
        spec="Электронщик"
        await call.message.answer("Электронщик - это специалист, занимающийся разработкой, производством, монтажом и обслуживанием электронных устройств и систем. Основные обязанности электронщика включают:\n"
        "Сборка электронных компонентов и узлов.\nНастройка и регулировка электронных устройств.\n Ремонт электронной техники.\nМонтаж и наладка электронных систем.\nТехническое обслуживание электронного оборудования.",reply_markup= SpecConfKeyBoard())
        await call.message.edit_reply_markup(reply_markup=None)
        await state.set_state(RegisterState.select_spec)

async def speciality_config(call: CallbackQuery, state: FSMContext):
    await call.answer()
    if call.data=="Да":
        User.create(UserName=data[0],UserSpec=spec)
        await call.message.edit_reply_markup(reply_markup=None)
        await call.message.answer(f"Поздравляю вы зачислены на 1 курс специальности ({spec})")
        await state.clear()
        
    elif call.data=="Нет":
        await call.message.edit_reply_markup(reply_markup=None)
        await call.message.answer("Выберете другую специальность",reply_markup=SpecKeyBoard())
        await state.set_state(RegisterState.register_spec)
