from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from tg_bot2 import states
from tg_bot2.keyboards.default import main_menu
from tg_bot2.utils import answer_education


async def collect_about(message: types.Message, state: FSMContext):
    data = await state.get_data()
    user = data["user"]
    user.about = message.text
    await state.update_data({"user": user})
    await states.Training.education.set()
    await message.answer("Отлично, какое у вас образование?", reply_markup=main_menu())


async def collect_education(message: types.Message, state: FSMContext):
    data = await state.get_data()
    user = data["user"]
    user.education = message.text
    await state.update_data({"user": user})
    await states.Training.age.set()
    await message.answer("Укажите свой возраст:", reply_markup=main_menu())


async def collect_age(message: types.Message, state: FSMContext):
    try:
        age = int(message.text)
    except:
        await message.answer("Неверно введен возраст, введите его иначе")
        return

    data = await state.get_data()
    user = data["user"]
    user.age = age
    user.training = True
    await user.save()
    await state.finish()
    await message.answer("Поздравляем, вы записались на обучение! Ожидайте, когда с вами свяжутся", reply_markup=main_menu())
    await answer_education(message, user)


def register_training_handlers(dp: Dispatcher):
    dp.register_message_handler(collect_about, state=states.Training.about)
    dp.register_message_handler(collect_education, state=states.Training.education)
    dp.register_message_handler(collect_age, state=states.Training.age)