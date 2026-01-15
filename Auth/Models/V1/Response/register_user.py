from pydantic import BaseModel, Field
from datetime import datetime


class RegisterUserResponse(BaseModel):
    id: str = Field(..., description="The user's unique identifier")
    first_name: str = Field(..., description="The user's first name")
    last_name: str = Field(..., description="The user's last name")
    email: str = Field(..., description="The user's email address")
    phone: str | None = Field(None, description="The user's phone number")
    password_hash: str = Field(..., description="The user's password hash")
    created_at: datetime = Field(..., description="Timestamp when the user was created")
    updated_at: datetime = Field(
        ..., description="Timestamp when the user was last updated"
    )
    verified: bool = Field(..., description="Whether the user is verified or not")

    model_config = {
        "json_schema_extra": {
            "example": {
                "id": "123e4567-e89b-12d3-a456-426655440000",
                "first_name": "John",
                "last_name": "Doe",
                "email": "H6u7o@example.com",
                "phone": "1234567890",
                "password_hash": "ewkfrh23otnkdackasndiqhri3nadawkfno32jr32ornkefsac",
                "created_at": "2023-08-01T12:34:56.789Z",
                "updated_at": "2023-08-01T12:34:56.789Z",
                "verified": False,
            }
        }
    }
