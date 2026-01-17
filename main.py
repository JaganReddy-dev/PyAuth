from fastapi import FastAPI
from dotenv import load_dotenv
from Auth.Apis import register_user
from Auth.Apis import login

load_dotenv()

app = FastAPI(
    title="PyAuth",
    version="1.0.0",
    description="Authentication and Authorization package for user identity management",
)

app.include_router(register_user.router)
app.include_router(login.router)
