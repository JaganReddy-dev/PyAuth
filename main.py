import bootstrap  # noqa: F401
from fastapi import FastAPI
from Auth.Apis.V1.tokens import router as tokens_router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    title="PyAuth",
    version="1.0.0",
    description="Authentication and Authorization package for user identity management",
)

app.include_router(tokens_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
