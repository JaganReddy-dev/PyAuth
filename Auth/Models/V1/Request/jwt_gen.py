from pydantic import BaseModel
from pydantic import EmailStr


class JWTGenRequest(BaseModel):
    sub: str
    email: EmailStr


class JWTSecret(BaseModel):
    jwt_secret: str
