from pydantic import BaseModel, EmailStr


class JWTGenRequest(BaseModel):
    sub: str
    email: EmailStr
