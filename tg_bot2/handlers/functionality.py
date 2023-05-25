
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from .collect_general_info import entrypoint
from tg_bot2 import states

async def consultation_handler(message: types.Message, state: FSMContext):
    await state.finish()
    user = await entrypoint(message, state, external_type="consultation")
    if user is not None:
        await state.set_data({"user":user})
        await states.Consultation.question.set()
        await message.answer("Вопрос по которому необходима консультация:")


async def training_handler(message: types.Message, state: FSMContext):
    await state.finish()
    user = await entrypoint(message, state, external_type="training")
    if user is not None:
        if not user.training:
            await state.set_data({"user":user})
            await states.Training.about.set()
            await message.answer("Кратко опишите себя:")
        else:
            await message.answer("Вы уже записаны на обучение, ожидайте когда с вами свяжутся")


async def analysis_handler(message: types.Message, state: FSMContext):
    await state.finish()
    user = await entrypoint(message, state, external_type="analysis")
    if user is not None:
        await state.set_data({"user":user})
        await states.Analysis.project_url.set()
        await message.answer("Ссылка на проект, который необходимо проанализировать:")


def register_functionality_handlers(dp: Dispatcher):
    dp.register_message_handler(consultation_handler, text="Получить консультацию", state="*")
    dp.register_message_handler(training_handler, text="Записаться на обучение", state="*")
    dp.register_message_handler(analysis_handler, text="Запросить анализ", state="*")