from Auth.Models.V1.Request.login_user import LoginUserRequest
from Auth.Utils.encrypt import hash_password
from Auth.Services.jwt_gen import create_jwt_token
from Auth.Services.refresh_token_gen import create_whole_refresh_token
from Auth.Utils.utc_now import utc_now
from datetime import timedelta
from Auth.Models.V1.Request.jwt_gen import JWTGenRequest


async def login_user_service(user: LoginUserRequest):
    hashed_password = hash_password(user.password)

    payload = JWTGenRequest(
        sub=user.user_id,
        email=user.email,
        roles=user.roles,
        iss=user.issuer,
        aud=user.audience,
        iat=utc_now(),
        exp=utc_now() + timedelta(minutes=5),
    )

    jwt_token = create_jwt_token(payload)
    refresh_token = create_whole_refresh_token(user.user_id)

    return {
        "hashed_password": hashed_password,
        "jwt_token": jwt_token,
        "refresh_token": refresh_token,
    }
