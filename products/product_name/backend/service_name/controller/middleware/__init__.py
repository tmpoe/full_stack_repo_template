from typing import Callable
import logging

from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import FastAPI, Request, Response

class LoggingMiddleware(BaseHTTPMiddleware):
    def __init__(self, app: FastAPI) -> None:
        super().__init__(app=app)

    async def __call__(self, request: Request, call_next: Callable) -> Response:
        logging.info("middleware called")
        response: Response = await call_next(request)

        return response