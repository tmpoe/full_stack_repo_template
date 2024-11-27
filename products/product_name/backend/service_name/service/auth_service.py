
from datetime import datetime, timedelta
import logging

import jwt
from service_name.domain.exception import ServiceException
from service_name.controller.authentication.consts import TOKEN_SECRET, TOKEN_ALGORITHM, TOKEN_EXPIRES_IN
from service_name.domain.service import IAuthService


class AuthService(IAuthService):
    async def get_current_user(token: str) -> dict:
        try:
            user = jwt.decode(token, TOKEN_SECRET, algorithm=TOKEN_ALGORITHM)
            return user
        except Exception as e:
            logging.error(f"Token exception: {e}")
            raise ServiceException(e)
        

    def create_access_token(data: dict) -> dict:
        to_encode = data.copy()

        expire = datetime.utcnow() + timedelta(minutes=TOKEN_EXPIRES_IN)

        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, TOKEN_SECRET, algorithm=TOKEN_ALGORITHM)
        return encoded_jwt


