from pydantic import BaseModel
from datetime import datetime
from pydantic import EmailStr


class JWTGenRequest(BaseModel):
    sub: str
    email: EmailStr
    roles: dict
    iss: str
    aud: str
    iat: datetime
    exp: datetime


class JWTSecret(BaseModel):
    jwt_secret: str
