from fastapi import APIRouter


def routes() -> APIRouter:
    """Register example routes."""
    router = APIRouter(prefix="")

    @router.get("/test")
    async def read_root() -> None:
        """Define example route."""
        return {"Hello": "World - 2nd version"}

    return router
