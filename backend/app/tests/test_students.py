import pytest
from fastapi import status

STUDENTS_ENDPOINT = "/students"


@pytest.mark.parametrize(
    "limit,len_expected",
    (
        (100, 2),
        (1, 1),
    )
)
@pytest.mark.usefixtures("students")
def test_read_students(client, limit, len_expected):
    r = client.get(f"{STUDENTS_ENDPOINT}?limit={limit}")
    assert r.status_code == status.HTTP_200_OK
    assert len(r.json()) == len_expected


def test_read_non_existing_students(client):
    r = client.get(STUDENTS_ENDPOINT)
    assert r.status_code == status.HTTP_200_OK
    assert len(r.json()) == 0


def test_read_student(client, student):
    r = client.get(f"{STUDENTS_ENDPOINT}/{student.id}")
    assert r.status_code == status.HTTP_200_OK
    data = r.json()
    assert data["student_name"] == student.student_name
    assert data["id"] == student.id


def test_read_non_existing_student(client):
    r = client.get(f"{STUDENTS_ENDPOINT}/1")
    assert r.status_code == status.HTTP_404_NOT_FOUND


def test_create_student(client):
    student = {"student_name": "Test Student 1", "class_tag": "T18", "age": 22}
    r = client.post(STUDENTS_ENDPOINT, json=student)
    assert r.status_code == status.HTTP_201_CREATED
    data = r.json()
    assert data["student_name"] == student["student_name"]
    assert "id" in data
    student_id = data["id"]

    r = client.get(f"{STUDENTS_ENDPOINT}/{student_id}")
    assert r.status_code == status.HTTP_200_OK
    data = r.json()
    assert data["student_name"] == student["student_name"]
    assert data["id"] == student_id


def test_create_existing_student_by_name(client):
    student = {"student_name": "Test Student 1", "class_tag": "T18", "age": 22}
    r = client.post(STUDENTS_ENDPOINT, json=student)
    assert r.status_code == status.HTTP_201_CREATED
    r = client.post(STUDENTS_ENDPOINT, json=student)
    assert r.status_code == status.HTTP_400_BAD_REQUEST


def test_create_minor_student(client):
    student = {"student_name": "Test Student 1", "class_tag": "T18", "age": 17}
    r = client.post(STUDENTS_ENDPOINT, json=student)
    assert r.status_code == status.HTTP_400_BAD_REQUEST


def test_update_student(client, student):
    updated_student = {"student_name": "Test Student Updated 1"}
    r = client.patch(
        f"{STUDENTS_ENDPOINT}/{student.id}",
        json=updated_student,
    )
    assert r.status_code == status.HTTP_200_OK
    data = r.json()
    assert "id" in data
    assert data["id"] == student.id
    assert data["class_tag"] == student.class_tag
    assert data["age"] == student.age
    assert data["student_name"] == updated_student["student_name"]


def test_update_non_existing_student(client):
    updated_student = {"student_name": "Test Student Updated 1"}
    r = client.patch(
        f"{STUDENTS_ENDPOINT}/1",
        json=updated_student,
    )
    assert r.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.usefixtures("students")
def test_update_existing_student_by_name(client):
    updated_student = {"student_name": "Test Student 2"}
    r = client.patch(
        f"{STUDENTS_ENDPOINT}/1",
        json=updated_student,
    )
    assert r.status_code == status.HTTP_400_BAD_REQUEST


def test_delete_student(client, student):
    r = client.delete(f"{STUDENTS_ENDPOINT}/{student.id}")
    assert r.status_code == status.HTTP_204_NO_CONTENT

    r = client.get(f"{STUDENTS_ENDPOINT}/{student.id}")
    assert r.status_code == status.HTTP_404_NOT_FOUND


def test_delete_non_existing_student(client):
    r = client.delete(f"{STUDENTS_ENDPOINT}/1")
    assert r.status_code == status.HTTP_404_NOT_FOUND
