from fastapi import FastAPI

from backend.router.example_routes import example_routes
from backend.router.user_routes import user_routes

app = FastAPI()

app.include_router(example_routes())
app.include_router(user_routes())

