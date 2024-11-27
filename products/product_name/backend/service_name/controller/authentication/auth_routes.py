from typing import Annotated

from dependency_injector import inject, Provide
from fastapi import Depends
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from service_name.controller.authentication.auth import create_access_token
from service_name.containers import Container
from service_name.domain.service.IUserManagementService import IUserManagementService
from service_name.infrastructure.fastapi_utils import APIRouter

def get_prefix() -> str:
    return "/user"

@inject
def auth_routes(user_management_service: IUserManagementService = Provide[Container.user_management_service]) -> APIRouter:
    """Define endpoints to control User related CRUD operations."""
    router = APIRouter(prefix=get_prefix())

    @router.post("/token")
    async def generate_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
        user = {"id": "test"}
    # Replace with your authentication logic
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )
        access_token = create_access_token(data={"sub": user["id"]})
        return {"access_token": access_token, "token_type": "bearer"}

