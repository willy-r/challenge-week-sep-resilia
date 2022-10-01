from fastapi import FastAPI
from dotenv import load_dotenv

from .routers import include_routers
from .middlewares import add_middlewares
from .database import engine, Base

load_dotenv()

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Middlewares.
add_middlewares(app)

# Routers.
include_routers(app)
