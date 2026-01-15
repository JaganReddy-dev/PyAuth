from pydantic import BaseModel, EmailStr, Field, field_validator
from typing import Optional
import re
import phonenumbers


class RegisterUserRequest(BaseModel):
    """
    Register a new user.

    - **first_name**: User's first name
    - **last_name**: User's last name
    - **email**: User's email address
    - **phone**: User's phone number (optional)
    - **password**: User's password
    """

    first_name: str = Field(
        ..., min_length=2, max_length=50, description="The user's first name"
    )
    last_name: str = Field(
        ..., min_length=2, max_length=50, description="The user's last name"
    )
    email: EmailStr = Field(..., max_length=100, description="The user's email address")
    phone: Optional[str] = Field(None, description="The user's phone number")
    password: str = Field(..., min_length=8, description="The user's password")

    @field_validator("first_name", "last_name")
    @classmethod
    def names_must_be_atleast_two_characters(cls, v: str) -> str:
        v = v.strip()
        if len(v) < 2:
            raise ValueError("Must be at least 2 characters long")

        if len(v) > 50:
            raise ValueError("Must be at most 50 characters long")

        if any(c.isdigit() for c in v):
            raise ValueError("Name must not contain numbers")

        return v

    @field_validator("email")
    @classmethod
    def normalize_email(cls, v: EmailStr) -> str:
        return v.lower()

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

    @field_validator("phone")
    @classmethod
    def phone_validator(cls, v: str) -> str:
        if v is None:
            return v

        try:
            phone_number = phonenumbers.parse(v, None)

            if not phonenumbers.is_valid_number(phone_number):
                raise ValueError("Invalid phone number format")
        except Exception as e:
            raise ValueError(f"Error parsing phone number: {str(e)}")

        result = phonenumbers.format_number(
            phone_number, phonenumbers.PhoneNumberFormat.E164
        )
        return result

    model_config = {
        "json_schema_extra": {
            "example": {
                "first_name": "John",
                "last_name": "Doe",
                "email": "H6u7o@example.com",
                "phone": "+1234567890",
                "password": "Password123!",
            }
        }
    }


class Message(BaseModel):
    message: str
