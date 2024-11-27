


from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from service_name.domain.service import IAuthService
from service_name.controller.authentication.consts import TOKEN_SECRET, TOKEN_ALGORITHM, TOKEN_EXPIRES_IN

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def get_current_user(token: str = Depends(oauth2_scheme), auth_service: IAuthService = Depends(Provide[Container.auth_service])):
    """Dependency to get the current user from the bearer token."""
    return auth_service.get_current_user(token) 

