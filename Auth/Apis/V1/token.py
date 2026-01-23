from fastapi import APIRouter, Body
from Auth.Services.V1.token_service import create_refresh_token, create_jwt_token
from Auth.Models.V1.Request.jwt_gen import JWTGenRequest

router = APIRouter(
    prefix="/token",
    tags=["RefreshToken"],
)


@router.post("/", summary="Create new jwt, refresh tokens")
async def create_token(user: JWTGenRequest) -> dict:
    jwt = create_jwt_token(user)
    refresh = create_refresh_token(user.sub)
    return {"jwt_token": jwt, "refresh_token": refresh}
