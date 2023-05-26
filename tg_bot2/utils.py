from aiogram import types
from tg_bot2.data.models import Analyze, User, Question
from tg_bot2.data.config import ADMINS


async def answer_to_admin(message: types.Message, text: str):
    for admin in ADMINS:
        await message.bot.send_message(admin, text)

async def answer_analyze(message: types.Message, analyze: Analyze):
    text = (
            f"Пользователь: {message.from_user.id}#@{message.from_user.username}#{analyze.user.name} оставил заявку на анализ проекта\n\n"
            f"Ссылка на проект: {analyze.project_url}\n"
            f"Приложение: {analyze.app}\n"
            f"Другая информация о предмете исследования: {analyze.other_info}\n\n"
            f"Предпочитаемый способ связи: {analyze.user.communication}\n"
            f"Номер телефона: {analyze.user.phone}\n"
            f"Почта: {analyze.user.email}\n"
            f"Город: {analyze.user.city}"
            )
    await answer_to_admin(message, text)

async def answer_education(message: types.Message, user: User):
    text = (
            f"Пользователь: {message.from_user.id}#@{message.from_user.username}#{user.name} оставил заявку на обучение\n\n"
            f"О себе: {user.about}\n"
            f"Образование: {user.education}\n"
            f"Возраст: {user.age}\n\n"
            f"Предпочитаемый способ связи: {user.communication}\n"
            f"Номер телефона: {user.phone}\n"
            f"Почта: {user.email}\n"
            f"Город: {user.city}"
            )
    await answer_to_admin(message, text)

async def answer_question(message: types.Message, question: Question):
    text = (
            f"Пользователь: {message.from_user.id}#@{message.from_user.username}#{question.user.name} задал вопрос:\n\n"
            f"{question.text}\n\n"
            f"Предпочитаемый способ связи: {question.user.communication}\n"
            f"Номер телефона: {question.user.phone}\n"
            f"Почта: {question.user.email}\n"
            f"Город: {question.user.city}"
            )
    await answer_to_admin(message, text)