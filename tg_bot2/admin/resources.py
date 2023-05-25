from fastapi_admin.app import app
from fastapi_admin.resources import Link
from fastapi_admin.resources import Field, Model
from tg_bot2.data.models import User, Analyze, Question
from fastapi_admin.widgets import filters, inputs
from fastapi_admin.file_upload import FileUpload
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
upload = FileUpload(uploads_dir=os.path.join(BASE_DIR, "static", "uploads"))


@app.register
class Home(Link):
    label = "Home"
    icon = "fas fa-home"
    url = "/admin"

@app.register
class UserResource(Model):
    label = "Пользователи"
    model = User
    icon = "fas fa-user"
    page_title = "Пользователи"
    filters = [
        filters.Search(
            name="telegram_username", label="Юзернейм", search_mode="contains", placeholder="Поиск по юзернейму"
        ),
    ]
    fields = [
        "id",
        "telegram_username",
        "name",
        "email",
        "phone",
        "city",
        "communication",
        "about",
        "education",
        Field(name="email", label="Email", input_=inputs.Email()),
    ]

@app.register
class AnalysisResource(Model):
    label = "Заявки на анализ"
    model = Analyze
    icon = "fas fa-user"
    page_title = "Заявки на анализ"
    filters = [
    ]
    fields = [
        "id",
        "user",
        Field("project_url", "Ссылка на проект"),
        "app",
        "other_info"
    ]

@app.register
class QuestionResource(Model):
    label = "Вопросы"
    model = Question
    icon = "fas fa-user"
    page_title = "Пользователи"
    filters = [
        filters.Search(
            name="telegram_username", label="Юзернейм", search_mode="contains", placeholder="Поиск по юзернейму"
        ),
    ]
    fields = [
        "id",
        "user",
        "text",
    ]