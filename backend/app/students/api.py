from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..dependencies import get_db
from . import schemas, crud

router = APIRouter(
    prefix="/students",
    tags=["Students"],
)


@router.get("", response_model=list[schemas.Student])
def read_students(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
):
    students = crud.get_students(db, skip, limit)
    return students


@router.get("/{student_id}", response_model=schemas.Student)
def read_student(student_id: int, db: Session = Depends(get_db)):
    db_student = crud.get_student_by_id(db, student_id)
    if db_student is None:
        raise HTTPException(
            detail=f"Student with ID {student_id} was not found",
            status_code=status.HTTP_404_NOT_FOUND,
        )
    return db_student


@router.post("", response_model=schemas.Student)
def create_student(
    student: schemas.StudentCreate,
    db: Session = Depends(get_db),
):
    db_student = crud.get_student_by_name(db, student.student_name)
    if db_student is not None:
        raise HTTPException(
            detail=f"Student with name {student.student_name} already registered",
            status_code=status.HTTP_400_BAD_REQUEST,
        )
    return crud.create_student(db, student)
