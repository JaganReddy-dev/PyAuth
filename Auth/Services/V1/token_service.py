from Auth.Utils.tokens.refresh_token.refresh_token_hash import create_refresh_token_hash
from Auth.Utils.tokens.refresh_token.raw_refresh_token import create_raw_refresh_token
from Auth.Utils.secret import get_required_secret
from datetime import datetime, timedelta, timezone
import uuid
from Auth.Utils.tokens.jwt_token import encoded_jwt, decoded_jwt
from Auth.Models.V1.Request.jwt_gen import JWTGenRequest
from Auth.Utils.utc_now import utc_now
from pprint import pprint  # noqa: F401


def get_refresh_token_expiry() -> int:
    return int(get_required_secret("REFRESH_TOKEN_EXPIRE_DAYS"))


def get_jwt_secret() -> str:
    return get_required_secret("SECRET")


def get_algorithm() -> str:
    return get_required_secret("ALGORITHM")


def create_refresh_token(user_id: str) -> dict:
    id = str(uuid.uuid4())
    token = create_refresh_token_hash(create_raw_refresh_token())
    now = utc_now()
    created_at = int(now.timestamp())
    expiry = int((now + timedelta(days=get_refresh_token_expiry())).timestamp())
    revoked = False

    document = {
        "id": id,
        "user_id": user_id,
        "token": token,
        "created_at": created_at,
        "expiry": expiry,
        "revoked": revoked,
    }
    return document


def create_jwt_token(payload: JWTGenRequest):
    document = {
        "sub": payload.sub,
        "email": str(payload.email),
        "iss": "localhost",
        "aud": "user",
    }
    jwt_token = encoded_jwt(document, get_jwt_secret(), get_algorithm())
    jwtDoc = {
        "token": jwt_token,
        "sub": payload.sub,
        "email": payload.email,
        "iss": document["iss"],
        "aud": document["aud"],
    }
    jwtDoc["iat"] = int((datetime.now(timezone.utc)).timestamp())
    jwtDoc["exp"] = int((datetime.now(timezone.utc) + timedelta(minutes=5)).timestamp())

    return jwtDoc


def verify_jwt_token(token):
    return decoded_jwt(token, get_jwt_secret(), get_algorithm(), aud="user")


# pprint(create_jwt_token(JWTGenRequest(sub="test", email="test@email.com")))
# pprint(
#     verify_jwt_token(
#         "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0IiwiZW1haWwiOiJ0ZXN0QGVtYWlsLmNvbSIsImlzcyI6ImxvY2FsaG9zdCIsImF1ZCI6InVzZXIifQ.7MYA3eQIcgyxtYHZUQBZtzAB5LkHi0HbGZnaZqXDPA8",
#         jwt_secret,
#         algorithm
#     )
# )
# pprint(
#     create_refresh_token(str(uuid.uuid4()))
# )
