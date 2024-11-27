from fastapi import FastAPI

from service_name.controller.example_routes import example_routes
from service_name.controller.user_routes import user_routes
from service_name.controller.authentication.auth_routes import auth_routes
from service_name.controller.middleware.LoggingMiddleware import LoggingMiddleware

app = FastAPI()

app.add_middleware(LoggingMiddleware)

app.include_router(example_routes())
app.include_router(user_routes())
app.include_router(auth_routes())

