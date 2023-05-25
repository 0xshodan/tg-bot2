
from aiogram.dispatcher.filters import CommandStart
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext

async def welcome_handler(message: types.Message, state: FSMContext):
    pass


def register_start_handler(dp: Dispatcher):
    dp.register_message_handler(welcome_handler, text="Начало", state="*")
    dp.register_message_handler(welcome_handler, CommandStart(), state="*")