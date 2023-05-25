from aiogram import executor
from loguru import logger
from tg_bot2.loader import dp
from tg_bot2.handlers import register_all_handlers

if __name__ == '__main__':
    register_all_handlers(dp)
    logger.info("Bot started")
    executor.start_polling(dp)
