import secrets
import hashlib


def create_refresh_token():
    raw_token = secrets.token_urlsafe(64)
    hashed_token = hashlib.sha256(raw_token.encode()).hexdigest()
    return {"hashed_token": hashed_token}
