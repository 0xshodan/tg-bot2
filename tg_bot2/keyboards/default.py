from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def start_keyboard():
    return ReplyKeyboardMarkup(resize_keyboard=True).row(
        KeyboardButton("Получить консультацию"), KeyboardButton("Записаться на обучение")
        ).row(
        KeyboardButton("Запросить анализ")
        ).row(
        KeyboardButton("Вернуться в начало")
        ).row(
        KeyboardButton("Перейти на сайт")
        )
