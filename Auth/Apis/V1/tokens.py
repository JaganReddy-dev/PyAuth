from fastapi import APIRouter, Body
from Auth.Services.V1.token_service import (
    create_refresh_token,
    create_jwt_token,
    revoke_refresh_token,
)
from Auth.Models.V1.Request.jwt_gen import JWTGenRequest
from Auth.Services.V1.token_service import verify_jwt_token
from Auth.Models.V1.Request.refresh_rt import RefreshToken

router = APIRouter(
    prefix="/tokens",
    tags=["Tokens"],
)


@router.post("/create", summary="Create new JWT, Refresh tokens")
async def create_token(user: JWTGenRequest) -> dict:
    jwt = create_jwt_token(user)
    refresh = create_refresh_token(user.sub)
    return {"jwt_token": jwt, "refresh_token": refresh}


@router.post("/verify", summary="Verify JWT token")
async def verify_token(token: str = Body(...)) -> dict:
    return verify_jwt_token(token)


@router.post("/refresh", summary="Refresh JWT and RT")
async def refresh_token(old_rt: RefreshToken = Body(...)) -> dict:
    revoked_rt = revoke_refresh_token(old_rt)
    new_jwt = create_jwt_token(JWTGenRequest(sub=old_rt.user_id))
    new_rt = create_refresh_token(old_rt.user_id)
    return {"revoked_rt": revoked_rt, "jwt_token": new_jwt, "refresh_token": new_rt}


@router.delete("/revoke", summary="Revoke Refresh Token")
async def revoke_token(old_rt: RefreshToken = Body(...)) -> dict:
    revoked_rt = revoke_refresh_token(old_rt)
    return revoked_rt.model_dump()
