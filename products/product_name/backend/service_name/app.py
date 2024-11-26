from fastapi import FastAPI
from starlette.middleware.base import BaseHTTPMiddleware

from controller.example_routes import example_routes
from controller.user_routes import user_routes
from service_name.controller.middleware import LoggingMiddleware

app = FastAPI()

app.add_middleware(BaseHTTPMiddleware, LoggingMiddleware)

app.include_router(example_routes())
app.include_router(user_routes())

