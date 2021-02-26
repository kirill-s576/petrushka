from pydantic import BaseModel
from pydantic.fields import FieldInfo
import datetime
from abc import ABC, abstractmethod


class Database:
    pass


class CustomField(FieldInfo, ABC):

    @abstractmethod
    def get_sql_query(self):
        pass


class IntegerField(CustomField):

    def __init__(self, default: int = None, null: bool = False):
        super().__init__(default=default)


class AbstractDatabaseModel(BaseModel):

    id: int = IntegerField()

    @property
    def table_name(self):
        return self.__class__.__name__.lower()

    def filter(self):
        pass


class CharField(CustomField):

    def __init__(self, default: str, max_length: int = 255, null: bool = False):
        super().__init__(default=default, max_length=max_length)


class TextField(CustomField):

    def __init__(self, default: str, null: bool = False):
        super().__init__(default=default)


class DatetimeField(CustomField):

    def __init__(self, default: datetime.datetime, null: bool = False):
        super().__init__(default=default)


class ForeignKeyField(CustomField):

    def __init__(self, model: AbstractDatabaseModel, null: bool = False):
        super().__init__()