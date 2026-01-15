from fastapi import status, APIRouter
from Auth.Models.V1.Request.register_user import RegisterUserRequest
from Auth.Services.register_user import resgister_user_service
from Auth.Models.V1.Response.register_user import RegisterUserResponse

router = APIRouter(
    prefix="/register",
    tags=["RegisterUser"],
)


@router.post(
    "/",
    response_model=RegisterUserResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Register a new user",
    description="Endpoint to register a new user in the system.",
)
async def register(user: RegisterUserRequest):
    user_data = await resgister_user_service(user)
    return user_data
