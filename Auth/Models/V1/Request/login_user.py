from pydantic import BaseModel, EmailStr, Field, field_validator
import re


class LoginUserRequest(BaseModel):
    email: EmailStr = Field(..., max_length=100, description="The user's email address")
    password: str = Field(..., min_length=8, description="The user's password")


@field_validator("password")
@classmethod
def password_validator(cls, v: str) -> str:
    if len(v) < 8:
        raise ValueError("Must be at least 8 characters long")

    if " " in v:
        raise ValueError("Password must not contain spaces")

    if not re.search(r"[A-Z]", v):
        raise ValueError("Password must contain at least one uppercase letter")

    if not re.search(r"[a-z]", v):
        raise ValueError("Password must contain at least one lowercase letter")

    if not re.search(r"\d", v):
        raise ValueError("Password must contain at least one digit")

    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', v):
        raise ValueError("Password must contain at least one special character")

    return v
