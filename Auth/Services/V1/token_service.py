from Auth.Utils.tokens.refresh_token.refresh_token_hash import create_refresh_token_hash
from Auth.Utils.tokens.refresh_token.raw_refresh_token import create_raw_refresh_token
from Auth.Utils.secret import get_required_secret
from datetime import timedelta
import uuid
from Auth.Utils.tokens.jwt_token import encoded_jwt, decoded_jwt
from Auth.Models.V1.Request.jwt_gen import JWTGenRequest
from Auth.Utils.utc_now import utc_now
from Auth.Models.V1.Request.refresh_rt import RefreshToken
from Auth.Models.V1.Request.verify_token import VerifyTokenRequest
from pprint import pprint  # noqa: F401
from jwt import exceptions as jwt_exceptions


def get_refresh_token_expiry() -> int:
    return int(get_required_secret("REFRESH_TOKEN_EXPIRE_DAYS"))


def get_jwt_secret() -> str:
    return get_required_secret("SECRET")


def get_algorithm() -> str:
    return get_required_secret("ALGORITHM")


def create_refresh_token(user_id: str) -> dict:
    if not user_id:
        raise ValueError({"detail": "User Id is required!"})
    raw_token = create_raw_refresh_token()
    refresh_token = create_refresh_token_hash(raw_token)
    id = str(uuid.uuid4())
    raw_token = raw_token
    now = utc_now()
    created_at = int(now.timestamp())
    expiry = int((now + timedelta(days=get_refresh_token_expiry())).timestamp())
    revoked = False

    document = {
        "id": id,
        "user_id": user_id,
        "raw_token": raw_token,
        "token": refresh_token,
        "created_at": created_at,
        "expiry": expiry,
        "revoked": revoked,
    }
    return document


def create_jwt_token(payload: JWTGenRequest):
    if not payload.sub.strip():
        raise ValueError({"detail": "Sub cannot be empty"})
    document = {
        "sub": payload.sub,
        "iss": "localhost",
        "aud": "user",
    }
    jwt_token = encoded_jwt(document, get_jwt_secret(), get_algorithm())
    now = utc_now()
    jwtDoc = {
        "token": jwt_token,
        "sub": payload.sub,
        "iss": document["iss"],
        "aud": document["aud"],
        "iat": int(now.timestamp()),
        "exp": int((now + timedelta(minutes=5)).timestamp()),
    }

    return jwtDoc


def verify_jwt_token(request: VerifyTokenRequest):
    if not request.token:
        raise ValueError({"detail": "Token is required"})
    try:
        decoded = decoded_jwt(
            request.token, get_jwt_secret(), get_algorithm(), aud="user"
        )
        return decoded
    except jwt_exceptions.DecodeError:
        raise ValueError("Invalid token format")
    except jwt_exceptions.ExpiredSignatureError:
        raise ValueError("Token has expired")
    except jwt_exceptions.InvalidAudienceError:
        raise ValueError("Token has invalid audience")
    except jwt_exceptions.PyJWTError as e:
        raise ValueError(f"JWT error: {str(e)}")


def revoke_refresh_token(token: RefreshToken):
    data = token.model_dump()
    data.update({"revoked": True, "expiry": int(utc_now().timestamp())})
    return RefreshToken(**data)


def verify_refresh_token(token: RefreshToken):
    if not token.token or not token.raw_token:
        raise ValueError({"detail": "Token and Raw Token are required"})
    hashed_token = create_refresh_token_hash(token.raw_token)
    if hashed_token == token.token:
        return True
    else:
        raise ValueError("Invalid refresh token")
