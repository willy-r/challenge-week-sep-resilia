import os

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database, drop_database
from fastapi.testclient import TestClient

from ..database import Base
from ..main import app
from ..dependencies import get_db
from ..students import crud as students_crud, schemas as students_schemas

DATABASE_PATH = os.path.join(os.path.normpath(".."), "test_db.sqlite3")
SQLALCHEMY_DATABASE_URL = f"sqlite:///{DATABASE_PATH}"


@pytest.fixture(scope="session")
def db_engine():
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
    )
    if not database_exists(engine.url):
        create_database(engine.url)
    Base.metadata.create_all(bind=engine)
    yield engine
    drop_database(engine.url)


@pytest.fixture
def test_db(db_engine):
    connection = db_engine.connect()
    connection.begin()
    db = sessionmaker(autocommit=False, autoflush=False, bind=connection)()
    yield db
    db.rollback()
    connection.close()


@pytest.fixture
def client(test_db):
    app.dependency_overrides[get_db] = lambda: test_db
    with TestClient(app) as api_client:
        yield api_client


@pytest.fixture
def students(test_db):
    students_crud.create_student(
        test_db,
        students_schemas.StudentCreate(
            student_name="Test Student 1",
            class_tag="T8",
            age=22,
        ),
    )
    students_crud.create_student(
        test_db,
        students_schemas.StudentCreate(
            student_name="Test Student 2",
            class_tag="T8",
            age=22,
        ),
    )


@pytest.fixture
def student(test_db):
    return students_crud.create_student(
        test_db,
        students_schemas.StudentCreate(
            student_name="Test Student 1",
            class_tag="T8",
            age=22,
        ),
    )
