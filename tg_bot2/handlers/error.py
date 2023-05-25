
from aiogram import types, Dispatcher
from loguru import logger

async def error(update: types.Update, exception: Exception):
    logger.exception(exception)
    logger.error(update)
    text = "Произошла ошибка, попробуйте еще раз или обратитесь в поддержку"
    try:
        await update.message.answer(text)
    except:
        await update.callback_query.message.answer(text)


def register_error_handler(dp: Dispatcher):
    dp.register_errors_handler(error)