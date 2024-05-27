from fastapi import FastAPI

from backend.router.base_routes import routes

app = FastAPI()

app.include_router(routes())

