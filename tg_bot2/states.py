from aiogram.dispatcher.filters.state import State, StatesGroup


class GeneralInfo(StatesGroup):
    name = State()
    email = State()
    phone = State()
    city = State()
    communication = State()


class Consultation(StatesGroup):
    question = State()

class Training(StatesGroup):
    description = State()
    education = State()
    age = State()

class Analysis(StatesGroup):
    project_url = State()
    app = State()
    other_info = State()
