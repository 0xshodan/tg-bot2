from environs import Env

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = env.list("ADMINS")  # Список админов
START_TEXT = env.str("START_TEXT")  # Приветственный текст
START_IMAGE = env.list("START_IMAGE")  # Тут у нас будет список из админов
