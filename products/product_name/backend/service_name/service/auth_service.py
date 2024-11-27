
import datetime as dt
import logging
from typing import Annotated

from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends

import jwt
from service_name.domain.exception import ServiceException
from service_name.controller.authentication.consts import TOKEN_SECRET, TOKEN_ALGORITHM, TOKEN_EXPIRES_IN
from service_name.domain.service.IAuthService import IAuthService


class AuthService(IAuthService):
    oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

    @staticmethod
    async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]) -> dict:
        try:
            user = jwt.decode(token, TOKEN_SECRET, algorithm=TOKEN_ALGORITHM)
            return user
        except Exception as e:
            logging.error(f"Token exception: {e}")
            raise ServiceException(e)
        
    @staticmethod
    def create_access_token(data: dict) -> dict:
        to_encode = data.copy()

        expire = dt.datetime.now(dt.timezone.utc) + dt.timedelta(minutes=TOKEN_EXPIRES_IN)

        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, TOKEN_SECRET, algorithm=TOKEN_ALGORITHM)
        return encoded_jwt


