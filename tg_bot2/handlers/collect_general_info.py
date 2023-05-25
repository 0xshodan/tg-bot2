
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext


async def entrypoint(message: types.Message, state: FSMContext):
    pass


def register_general_info_handlers(dp: Dispatcher):
    pass