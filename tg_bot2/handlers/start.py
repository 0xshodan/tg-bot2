
from aiogram.dispatcher.filters import CommandStart
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from tg_bot2.data import config

async def welcome_handler(message: types.Message, state: FSMContext):
    await state.finish()
    photo = types.InputFile(config.START_IMAGE_PATH)
    await message.answer_photo(photo, config.START_TEXT)


def register_start_handler(dp: Dispatcher):
    dp.register_message_handler(welcome_handler, text="Начало", state="*")
    dp.register_message_handler(welcome_handler, CommandStart(), state="*")