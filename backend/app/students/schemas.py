from datetime import datetime

from pydantic import BaseModel


class StudentBase(BaseModel):
    student_name: str
    class_tag: str
    age: int


class StudentCreate(StudentBase):
    pass


class StudentUpdate(BaseModel):
    student_name: str | None = None
    class_tag: str | None = None
    age: int | None = None


class Student(StudentBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
