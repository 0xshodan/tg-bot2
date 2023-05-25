from environs import Env
from os.path import isfile
# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()

BOT_TOKEN: str = env.str("BOT_TOKEN")
ADMINS: list[str] = env.list("ADMINS")  # Список админов
START_TEXT: str = env.str("START_TEXT")  # Приветственный текст
START_IMAGE_PATH: str = env.str("START_IMAGE_PATH")  # Тут у нас будет список из админов
if not isfile(START_IMAGE_PATH):
    raise FileNotFoundError("Ошибка: неверно указан путь для приветсвенного изображения")