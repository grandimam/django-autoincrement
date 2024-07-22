from django.db import models
from django.db import connection


class AutoIncrementField(models.IntegerField):
    def __init__(self, sequence_name=None, *args, **kwargs):
        if not sequence_name:
            raise ValueError("AutoIncrementField requires a sequence_name argument.")
        self.sequence_name = sequence_name
        super().__init__(*args, **kwargs)

    def db_type(self, conn):
        return 'integer'

    def pre_save(self, model_instance, add):
        if getattr(model_instance, self.attname) is None:
            with connection.cursor() as cursor:
                cursor.execute(f"SELECT nextval('{self.sequence_name}')")
                value = cursor.fetchone()[0]
                setattr(model_instance, self.attname, value)
        return super().pre_save(model_instance, add)
