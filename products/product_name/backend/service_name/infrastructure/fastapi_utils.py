
from typing import Any
from fastapi.types import DecoratedCallable


class APIRouter(FastAPIRouter):
    def api_route(self, path: str, *, include_in_schema: bool = True,**kwargs: Any):
        if path.endswith('/'):
            path = path[:-1]

        add_path = super().api_route(path, include_in_schema, **kwargs)

        alternate_path = f"{path}/"
        add_alternate_path = super().api_route(alternate_path, include_in_schema, **kwargs)

        def decorator(func: DecoratedCallable) -> DecoratedCallable:
            add_alternate_path(func)
            return add_path(func)
        
        return decorator