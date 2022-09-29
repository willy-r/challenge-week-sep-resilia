from sqlalchemy.orm import Session

from . import models, schemas


def get_student_by_id(db: Session, student_id: int) -> models.Student | None:
    return db.query(models.Student).get(student_id)


def get_student_by_name(db: Session, student_name: str) -> models.Student | None:
    return db.query(models.Student).filter_by(student_name=student_name).first()


def get_students(
    db: Session, skip: int = 0, limit: int = 100
) -> list[models.Student]:
    query = db.query(models.Student).order_by(models.Student.id)
    # @TODO: implement search by filters.
    # if filters:
    #     query = query.filter_by(**filters)
    return query.offset(skip).limit(limit).all()


def create_student(
    db: Session, new_student: schemas.StudentCreate
) -> models.Student:
    db_student = models.Student(**new_student.dict())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student
