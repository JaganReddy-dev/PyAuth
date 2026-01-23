from uuid import UUID
from pydantic import BaseModel


class RefreshToken(BaseModel):
    id: UUID
    user_id: str
    token: str
    created_at: int
    expiry: int
    revoked: bool
