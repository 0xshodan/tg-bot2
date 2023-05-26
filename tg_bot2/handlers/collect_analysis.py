from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from tg_bot2 import states
from tg_bot2.data.models import Analyze
from tg_bot2.keyboards.default import skip, main_menu
from tg_bot2.utils import answer_analyze


async def collect_project_url(message: types.Message, state: FSMContext):
    data = await state.get_data()
    user = data["user"]

    analyze = Analyze(user=user)
    analyze.project_url = message.text
    await state.update_data({"analyze": analyze})

    await states.Analysis.app.set()
    await message.answer("Приложение (если есть):", reply_markup=skip())

async def collect_app(message: types.Message, state: FSMContext):
    if message.text != "Пропустить":
        data = await state.get_data()
        analyze = data["analyze"]

        analyze.app = message.text
        await state.update_data({"analyze": analyze})

    await states.Analysis.other_info.set()
    await message.answer("Другая информация о предмете исследования:", reply_markup=skip())

async def collect_other_info(message: types.Message, state: FSMContext):
    data = await state.get_data()
    analyze = data["analyze"]
    if message.text != "Пропустить":
        analyze.other_info = message.text

    await analyze.save()
    await state.finish()

    await message.answer("Ваша заявка принята, ожидайте, когда с вами свяжутся", reply_markup=main_menu())
    await answer_analyze(message, analyze)


def register_analysis_handlers(dp: Dispatcher):
    dp.register_message_handler(collect_project_url, state=states.Analysis.project_url)
    dp.register_message_handler(collect_app, state=states.Analysis.app)
    dp.register_message_handler(collect_other_info, state=states.Analysis.other_info)