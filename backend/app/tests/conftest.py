import os
import pytest
from fastapi.testclient import TestClient

from ..main import app


@pytest.fixture
def client(monkeypatch):
    monkeypatch.setenv("DATABASE_URL", "sqlite:///./test.sqlite3")
    return TestClient(app)
