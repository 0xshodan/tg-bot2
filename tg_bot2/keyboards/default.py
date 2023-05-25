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

main_menu_button = KeyboardButton("Вернуться в начало")
def main_menu():
    return ReplyKeyboardMarkup(resize_keyboard=True).row(main_menu_button)

def skip():
    return ReplyKeyboardMarkup(resize_keyboard=True).row(
        KeyboardButton("Пропустить")).row(main_menu_button)