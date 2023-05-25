from tortoise.models import Model
from tortoise import fields



class User(Model):
    id = fields.BigIntField(pk=True)

    telegram_first_name = fields.CharField(max_length=64, null=True)
    telegram_last_name = fields.CharField(max_length=64, null=True)
    telegram_username = fields.CharField(max_length=32, null=True)

    name = fields.TextField(null=True)
    email = fields.CharField(max_length=255, null=True)
    phone = fields.CharField(max_length=255, null=True)
    city = fields.CharField(max_length=255, null=True)
    communication = fields.CharField(max_length=255, null=True)

    about = fields.TextField(null=True)
    education = fields.TextField(null=True)
    age = fields.SmallIntField(null=True)
    training = fields.BooleanField(default=False)



    def __str__(self):
        return self.telegram_username

class Question(Model):
    user = fields.ForeignKeyField("models.User", "questions")
    text = fields.TextField()

class Analyze(Model):
    user = fields.ForeignKeyField("models.User", "analyzes")
    project_url = fields.CharField(max_length=1024, null=True)
    app = fields.CharField(max_length=1024, null=True)
    other_info = fields.TextField(null=True)