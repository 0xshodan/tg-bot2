from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from tg_bot2 import states
from tg_bot2.data.models import Question
from tg_bot2.keyboards.default import main_menu

async def collect_question(message: types.Message, state: FSMContext):
    data = await state.get_data()
    user = data["user"]
    await Question.create(user=user, text=message.text)
    await message.answer("Все готово! Ваш вопрос доставлен", reply_markup=main_menu())

def register_question_handler(dp: Dispatcher):
    dp.register_message_handler(collect_question, state=states.Consultation.question)