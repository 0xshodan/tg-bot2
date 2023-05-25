from tortoise.models import Model
from tortoise import fields

class User(Model):
    id = fields.IntField(pk=True)
    telegram_name = fields.TextField()
    telegram_name = fields.TextField()

    def __str__(self):
        return self.name

