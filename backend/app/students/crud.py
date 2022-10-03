from sqlalchemy import case, literal_column, and_, func
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


def get_students_ages(db: Session) -> dict[str, int]:
    case_expression = case(
        (
            and_(models.Student.age >= 18, models.Student.age <= 21),
            literal_column("'De 18 a 21 anos'")
        ),
        (
            and_(models.Student.age >= 22, models.Student.age <= 25),
            literal_column("'De 22 a 25 anos'")
        ),
        (
            and_(models.Student.age >= 26, models.Student.age <= 29),
            literal_column("'De 26 a 29 anos'")
        ),
        (
            and_(models.Student.age >= 30, models.Student.age <= 33),
            literal_column("'De 30 a 33 anos'")
        ),
        else_=literal_column("'Acima de 33 anos'")
    ).label(
        "age_cases"
    )
    data = db.query(case_expression, func.count()).group_by("age_cases").all()
    return {
        desc: count
        for desc, count in data    
    }


def create_student(
    db: Session, new_student: schemas.StudentCreate
) -> models.Student:
    db_student = models.Student(**new_student.dict())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student


def update_student(
    db: Session, student_id: int, student: schemas.StudentUpdate
) -> models.Student:
    db_student = get_student_by_id(db, student_id)
    stored_student = schemas.Student(**db_student.__dict__)
    updated_student = stored_student.copy(update=student.dict(exclude_unset=True))
    db.query(models.Student).filter_by(id=student_id).update(updated_student.dict())
    db.commit()
    db.refresh(db_student)
    return db_student


def delete_student_by_id(db: Session, student_id: int) -> None:
    db.query(models.Student).filter_by(id=student_id).delete()
    db.commit()
