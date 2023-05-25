from aiogram import executor
from loguru import logger
from tg_bot2.loader import dp
from tg_bot2.handlers import register_all_handlers
from tortoise import Tortoise, run_async


async def init_db():
    await Tortoise.init(
        db_url='sqlite://db.sqlite3',
        modules={'models': ['tg_bot2.data.models']}
    )
    await Tortoise.generate_schemas()


if __name__ == '__main__':
    run_async(init_db())
    register_all_handlers(dp)
    logger.info("Bot started")
    executor.start_polling(dp)
