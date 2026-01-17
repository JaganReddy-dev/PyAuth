import os
from Auth.Utils.tokens.jwt_token import encoded_jwt, decoded_jwt
from Auth.Utils.tokens.refresh_token.secret import create_secret
from Auth.Models.V1.Request.jwt_gen import JWTGenRequest

create_secret()
jwt_secret = os.getenv("SECRET")
algorithm = os.getenv("ALGORITHM")
refresh_token_expiry = os.getenv("REFRESH_TOKEN_EXPIRE_DAYS")


def create_jwt_token(payload: JWTGenRequest):
    return encoded_jwt(payload, jwt_secret, algorithm)


def verify_jwt_token(token, jwt_secret, algorithm):
    return decoded_jwt(token, jwt_secret, algorithm)


# jwt_token = create_jwt_token(payload, jwt_secret, algorithm)
# result = verify_jwt_token(jwt_token, jwt_secret, algorithm)
