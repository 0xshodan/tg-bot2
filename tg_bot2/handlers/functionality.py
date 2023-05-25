
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from tg_bot2.data import config
from tg_bot2.keyboards.default import start_keyboard
from .collect_general_info import entrypoint


async def consultation_handler(message: types.Message, state: FSMContext):
    user = await entrypoint(message, state, external_type="consultation")
    if user is not None:
        pass


async def training_handler(message: types.Message, state: FSMContext):
    await state.finish()
    photo = types.InputFile(config.START_IMAGE_PATH)
    await message.answer_photo(photo, config.START_TEXT,reply_markup=start_keyboard())


async def analysis_handler(message: types.Message, state: FSMContext):
    await state.finish()
    photo = types.InputFile(config.START_IMAGE_PATH)
    await message.answer_photo(photo, config.START_TEXT,reply_markup=start_keyboard())


def register_functionality_handlers(dp: Dispatcher):
    dp.register_message_handler(consultation_handler, text="Получить консультацию", state="*")
    dp.register_message_handler(training_handler, text="Записаться на обучение", state="*")
    dp.register_message_handler(analysis_handler, text="Запросить анализ", state="*")