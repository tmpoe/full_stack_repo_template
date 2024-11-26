from datetime import datetime, timedelta
from typing import Annotated

from dependency_injector import inject, Provide
from fastapi import Depends
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
import jwt

from service_name.controller.authentication.consts import TOKEN_EXPIRES_IN, TOKEN_ALGORITHM, TOKEN_SECRET
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
        user = "user"
    # Replace with your authentication logic
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        access_token_expires = timedelta(minutes=TOKEN_EXPIRES_IN)

        access_token = create_access_token(
            data={"sub": user.id}, expires_delta=access_token_expires
        )
        return {"access_token": access_token, "token_type": "bearer"}



def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, TOKEN_SECRET, algorithm=TOKEN_ALGORITHM)
    return encoded_jwt
