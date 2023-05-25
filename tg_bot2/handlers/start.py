
from aiogram.dispatcher.filters import CommandStart
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from tg_bot2.data import config
from tg_bot2.data.models import User
from tg_bot2.keyboards.default import start_keyboard


async def welcome_handler(message: types.Message, state: FSMContext):
    User.get_or_create(
        id=message.from_user.id,
        defaults={
            "id":message.from_user.id,
            "telegram_first_name":message.from_user.first_name,
            "telegram_last_name":message.from_user.last_name,
            "telegram_username":message.from_user.username,
            }
            )
    await state.finish()
    photo = types.InputFile(config.START_IMAGE_PATH)
    await message.answer_photo(photo, config.START_TEXT,reply_markup=start_keyboard())


def register_start_handler(dp: Dispatcher):
    dp.register_message_handler(welcome_handler, text="Вернуться в начало", state="*")
    dp.register_message_handler(welcome_handler, CommandStart(), state="*")