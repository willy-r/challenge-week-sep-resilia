from fastapi import APIRouter, Depends, HTTPException, Response, status
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
            detail="Estudante não foi encontrado",
            status_code=status.HTTP_404_NOT_FOUND,
        )
    return db_student


@router.post(
    "",
    response_model=schemas.Student,
    status_code=status.HTTP_201_CREATED,
)
def create_student(
    student: schemas.StudentCreate,
    db: Session = Depends(get_db),
):
    db_student = crud.get_student_by_name(db, student.student_name)
    if db_student is not None:
        raise HTTPException(
            detail=f"Estudante com o nome {student.student_name} já está cadastrado",
            status_code=status.HTTP_400_BAD_REQUEST,
        )
    if student.age < 18:
        raise HTTPException(
            detail=f"Estudante precisa ser maior de idade",
            status_code=status.HTTP_400_BAD_REQUEST,
        )
    return crud.create_student(db, student)


@router.patch("/{student_id}", response_model=schemas.Student)
def update_student(
    student_id: int,
    student: schemas.StudentUpdate,
    db: Session = Depends(get_db),
):
    db_student = crud.get_student_by_id(db, student_id)
    if db_student is None:
        raise HTTPException(
            detail=f"Estudante não foi encontrado",
            status_code=status.HTTP_404_NOT_FOUND,
        )
    if student.student_name != db_student.student_name:
        if (student.student_name is not None and
                crud.get_student_by_name(db, student.student_name)) is not None:
            raise HTTPException(
                detail=f"Estudante com o nome {student.student_name} já está cadastrado",
                status_code=status.HTTP_400_BAD_REQUEST,
            )
    return crud.update_student(db, student_id, student)


@router.delete(
    "/{student_id}",
    response_class=Response,
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_student(
    student_id: int,
    db: Session = Depends(get_db),
):
    db_student = crud.get_student_by_id(db, student_id)
    if db_student is None:
        raise HTTPException(
            detail=f"Estudante não foi encontrado",
            status_code=status.HTTP_404_NOT_FOUND,
        )
    crud.delete_student_by_id(db, student_id)
