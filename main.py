from fastapi import FastAPI
from Auth.Apis import register_user

app = FastAPI(
    title="PyAuth",
    version="1.0.0",
    description="Authentication and Authorization package for user identity management",
)

app.include_router(register_user.router)
