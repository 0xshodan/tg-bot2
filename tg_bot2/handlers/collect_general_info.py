
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from tg_bot2.data.models import User
from tg_bot2 import states
from typing import Optional


async def entrypoint(message: types.Message, state: FSMContext, external_type: str = "") -> Optional[User]:
    user = await User.get(id=message.from_user.id)
    await state.set_data({"user": user, "type":external_type})
    if user.name is None:
        await states.GeneralInfo.name.set()
        await message.answer("Для начала введите своё имя:")
    elif user.email is None:
        await states.GeneralInfo.email.set()
        await message.answer("Теперь укажите почту")
    elif user.phone is None:
        await states.GeneralInfo.phone.set()
        await message.answer("Укажите ваш телефон")
    elif user.city is None:
        await states.GeneralInfo.city.set()
        await message.answer("Ваш город:")
    elif user.communication is None:
        await states.GeneralInfo.communication.set()
        await message.answer("Предпочитаемый способ связи (телеграм/телефон/почта):")
    else:
        return user

async def collect_name(message: types.Message, state: FSMContext):
    data = await state.get_data()
    user = data["user"]
    user.name = message.text
    await states.GeneralInfo.email.set()
    await message.answer("Теперь укажите почту")

async def collect_email(message: types.Message, state: FSMContext):
    data = await state.get_data()
    user = data["user"]
    user.email = message.text
    await states.GeneralInfo.phone.set()
    await message.answer("Укажите ваш телефон")

async def collect_phone(message: types.Message, state: FSMContext):
    data = await state.get_data()
    user = data["user"]
    user.phone = message.text
    await states.GeneralInfo.city.set()
    await message.answer("Ваш город:")

async def collect_city(message: types.Message, state: FSMContext):
    data = await state.get_data()
    user = data["user"]
    user.city = message.text
    await states.GeneralInfo.communication.set()
    await message.answer("Предпочитаемый способ связи (телеграм/телефон/почта):")

async def collect_communication(message: types.Message, state: FSMContext):
    data = await state.get_data()
    user = data["user"]
    user.communication = message.text
    if data["type"] == "consultation":
        await states.Consultation.question.set()
        await message.answer("Вопрос по которому необходима консультация: ")
    elif data["type"] == "training":
        await states.Training.description.set()
    elif data["type"] == "analysis":
        await states.Analysis.project_url.set()

def register_general_info_handlers(dp: Dispatcher):
    dp.register_message_handler(collect_name, state=states.GeneralInfo.name)
    dp.register_message_handler(collect_email, state=states.GeneralInfo.email)
    dp.register_message_handler(collect_phone, state=states.GeneralInfo.phone)
    dp.register_message_handler(collect_city, state=states.GeneralInfo.city)
    dp.register_message_handler(collect_communication, state=states.GeneralInfo.communication)