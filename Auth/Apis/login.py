from fastapi import APIRouter
from Auth.Models.V1.Request.login_user import LoginUserRequest
from Auth.Services.login_user import login_user_service

router = APIRouter(
    prefix="/login",
    tags=["Login"],
)


@router.post(
    "/",
    summary="Login a user",
    description="Endpoint to login a user in the system.",
)
async def login(user: LoginUserRequest):
    return await login_user_service(user)
