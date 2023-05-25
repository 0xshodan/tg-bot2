from aiogram import Dispatcher
from .start import register_start_handler
from .error import register_error_handler
from .functionality import register_functionality_handlers


def register_all_handlers(dp: Dispatcher):
    register_start_handler(dp)
    register_error_handler(dp)
    register_functionality_handlers(dp)
