from fastapi import APIRouter


def example_routes() -> APIRouter:
    """Register example routes."""
    router = APIRouter(prefix="")

    @router.get("/")
    async def root() -> None:
        """Define example route."""
        return {"Tec Exchange XII": "Welcome"}


    @router.get("/test")
    async def test() -> None:
        """Define example route."""
        return {"Tec Exchange XII": "Welcome on /test"}

    return router
