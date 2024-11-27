from typing import Annotated
from fastapi import  Query
from service_name.infrastructure.fastapi_utils import APIRouter


def example_routes() -> APIRouter:
    """Register example routes."""
    router = APIRouter(prefix="/example")

    @router.get("/")
    def root() -> None:
        """Define example route."""
        return {"Tec Exchange XII": "Welcome"}


    @router.get("/test")
    def test(test_query_param: Annotated[str, Query(...)]) -> None:
        """Define example route."""
        return {"Tec Exchange XII": "Welcome on /test"}

    return router
