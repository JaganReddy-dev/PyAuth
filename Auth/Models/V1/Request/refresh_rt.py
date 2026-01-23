from uuid import UUID
from pydantic import BaseModel, Field


class RefreshToken(BaseModel):
    id: UUID
    user_id: str
    token: str
    created_at: int
    expiry: int
    revoked: bool = Field(default=False)
