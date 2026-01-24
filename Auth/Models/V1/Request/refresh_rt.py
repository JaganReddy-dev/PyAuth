from uuid import UUID
from pydantic import BaseModel, Field


class RefreshToken(BaseModel):
    id: UUID
    user_id: str
    raw_token: str
    token: str
    created_at: int
    expiry: int
    revoked: bool = Field(default=False)
