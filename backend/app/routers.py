from fastapi import FastAPI

from .students.api import router as students_router


def include_routers(app: FastAPI) -> None:
    app.include_router(students_router)
