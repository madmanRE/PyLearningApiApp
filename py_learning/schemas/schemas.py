from pydantic import BaseModel, validator
from typing import Optional
from decimal import Decimal


class PersonBase(BaseModel):
    name: str
    email: str
    password: str


class SchemaAuthor(BaseModel):
    class Config:
        orm_mode = True


class SchemaUser(PersonBase):
    class Config:
        orm_mode = True


class BaseCourse(BaseModel):
    title: str
    description: Optional[str]


class SchemaCourse(BaseCourse):
    price: Decimal
    author_id: int


class SchemaModule(BaseCourse):
    difficulty: Optional[int]
    course_id: int

    @validator("difficulty")
    def validate_difficulty(cls, value):
        if value is not None and (value < 1 or value > 5):
            raise ValueError("Difficulty must be between 1 and 5")
        return value


class SchemaLesson(BaseCourse):
    duration: int
    module_id: int
