from pydantic import BaseModel


class JWTGenRequest(BaseModel):
    sub: str
