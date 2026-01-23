import secrets


def create_raw_refresh_token() -> str:
    raw_token = secrets.token_urlsafe(64)
    return str(raw_token)
