

from typing import Annotated

import jwt
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from service_name.controller.authentication.consts import TOKEN_SECRET, TOKEN_ALGORITHM

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    try:
        user = jwt.decode(token, TOKEN_SECRET, algorithm=TOKEN_ALGORITHM)
        return user
    except jwt.InvalidTokenError:
        raise Exception("Invalid token")



