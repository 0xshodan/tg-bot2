from aiogram import Dispatcher
from .start import register_start_handler
from .error import register_error_handler
from .functionality import register_functionality_handlers
from .collect_general_info import register_general_info_handlers
from .collect_consultaion import register_question_handler
from .collect_training import register_training_handlers
from .collect_analysis import register_analysis_handlers

def register_all_handlers(dp: Dispatcher):
    register_start_handler(dp)
    register_error_handler(dp)
    register_functionality_handlers(dp)
    register_general_info_handlers(dp)
    register_question_handler(dp)
    register_training_handlers(dp)
    register_analysis_handlers(dp)
