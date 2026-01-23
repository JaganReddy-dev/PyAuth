import bootstrap  # noqa: F401
from fastapi import FastAPI
from Auth.Apis.V1.token import router as token_router


app = FastAPI(
    title="PyAuth",
    version="1.0.0",
    description="Authentication and Authorization package for user identity management",
)

app.include_router(token_router)
