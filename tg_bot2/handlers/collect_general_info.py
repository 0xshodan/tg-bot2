
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from tg_bot2.data.models import User
from tg_bot2 import states
from typing import Optional
from tg_bot2.keyboards.default import main_menu

async def entrypoint(message: types.Message, state: FSMContext, external_type: str = "") -> Optional[User]:
    user = await User.get(id=message.from_user.id)
    await state.set_data({"user": user, "type":external_type})
    if user.name is None:
        await states.GeneralInfo.name.set()
        await message.answer("Для начала введите своё имя:", reply_markup=main_menu())
    elif user.email is None:
        await states.GeneralInfo.email.set()
        await message.answer("Теперь укажите почту", reply_markup=main_menu())
    elif user.phone is None:
        await states.GeneralInfo.phone.set()
        await message.answer("Укажите ваш телефон", reply_markup=main_menu())
    elif user.city is None:
        await states.GeneralInfo.city.set()
        await message.answer("Ваш город:", reply_markup=main_menu())
    elif user.communication is None:
        await states.GeneralInfo.communication.set()
        await message.answer("Предпочитаемый способ связи (телеграм/телефон/почта):", reply_markup=main_menu())
    else:
        return user

async def collect_name(message: types.Message, state: FSMContext):
    data = await state.get_data()
    user = data["user"]
    user.name = message.text
    await state.update_data({"user": user})
    await states.GeneralInfo.email.set()
    await message.answer("Теперь укажите почту", reply_markup=main_menu())

async def collect_email(message: types.Message, state: FSMContext):
    data = await state.get_data()
    user = data["user"]
    user.email = message.text
    await state.update_data({"user": user})
    await states.GeneralInfo.phone.set()
    await message.answer("Укажите ваш телефон", reply_markup=main_menu())

async def collect_phone(message: types.Message, state: FSMContext):
    data = await state.get_data()
    user = data["user"]
    user.phone = message.text
    await state.update_data({"user": user})
    await states.GeneralInfo.city.set()
    await message.answer("Ваш город:", reply_markup=main_menu())

async def collect_city(message: types.Message, state: FSMContext):
    data = await state.get_data()
    user = data["user"]
    user.city = message.text
    await state.update_data({"user": user})
    await states.GeneralInfo.communication.set()
    await message.answer("Предпочитаемый способ связи (телеграм/телефон/почта):", reply_markup=main_menu())

async def collect_communication(message: types.Message, state: FSMContext):
    data = await state.get_data()
    user = data["user"]
    user.communication = message.text
    await state.update_data({"user": user})
    await user.save()
    if data["type"] == "consultation":
        await states.Consultation.question.set()
        await message.answer("Вопрос по которому необходима консультация:")
    elif data["type"] == "training":
        await states.Training.about.set()
        await message.answer("Почти все готово! Теперь опишите себя:")
    elif data["type"] == "analysis":
        await states.Analysis.project_url.set()
        await message.answer("Ссылка на проект, который необходимо проанализировать:")

def register_general_info_handlers(dp: Dispatcher):
    dp.register_message_handler(collect_name, state=states.GeneralInfo.name)
    dp.register_message_handler(collect_email, state=states.GeneralInfo.email)
    dp.register_message_handler(collect_phone, state=states.GeneralInfo.phone)
    dp.register_message_handler(collect_city, state=states.GeneralInfo.city)
    dp.register_message_handler(collect_communication, state=states.GeneralInfo.communication)