from fastapi import FastAPI
from dotenv import load_dotenv

from routers import include_routers

load_dotenv()

app = FastAPI()

# Routers.
include_routers(app)
