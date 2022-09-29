from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func

from ..database import Base


class Student(Base):
    __tablename__ = "resilia_students"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    student_name = Column(String(length=50), unique=True, index=True, nullable=False)
    class_tag = Column(String(5), nullable=False)
    age = Column(Integer, nullable=False)

    created_at = Column(DateTime(timezone=True), default=datetime.utcnow())
    updated_at = Column(
        DateTime(timezone=True),
        default=datetime.utcnow(),
        onupdate=datetime.utcnow(),
    )
