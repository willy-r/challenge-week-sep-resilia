from fastapi import status

STUDENTS_ENDPOINT = "/students"


def test_read_students(client):
    r = client.get(STUDENTS_ENDPOINT)
    assert r.status_code == status.HTTP_200_OK
