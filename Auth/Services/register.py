from Auth.DB.mongo_client import users
from fastapi import HTTPException, status, APIRouter
from Auth.Models.V1.Request.register_user import RegisterUser

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)


@router.post("/register")
async def register_user(user: RegisterUser):
    user_details = users.find_one({"email": str(user.email)})
    if user_details:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email already exists.",
        )

    users.insert_one(user)
    return {"message": "User registered successfully."}
