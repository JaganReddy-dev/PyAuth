from pydantic import BaseModel


class VerifyTokenResponse(BaseModel):
    sub: str
    iss: str
    aud: str


class ErrorResponse(BaseModel):
    detail: str
