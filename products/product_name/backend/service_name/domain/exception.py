
from functools import wraps
from typing import Any, Callable, TypeVar
from fastapi import HTTPException


RT = TypeVar("RT")

class ServiceException(Exception):
    ...

def translate_service_exception(func: Callable[..., RT]):
    @wraps(func)
    def decorator(*args: Any, **kwargs: Any) -> RT:
        try:
            return func(*args, **kwargs)
        except ServiceException as e:
            raise HTTPException(status_code=e.status_code, detail=e.detail) from e
    return decorator
        