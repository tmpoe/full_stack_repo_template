
from fastapi import Depends
from service_name.service.auth_service import AuthService

async def get_current_user(token: str = Depends(lambda: AuthService.oauth2_scheme)):
    return await AuthService.get_current_user(token)