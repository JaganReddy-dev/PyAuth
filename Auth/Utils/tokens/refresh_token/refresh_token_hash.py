import hashlib
from Auth.Utils.secret import get_required_secret


def create_refresh_token_hash(raw_token: str) -> bytes:
    if not raw_token:
        raise ValueError("raw_token is required")
    secret = get_required_secret("REFRESH_TOKEN_SECRET")
    secretbytes = hashlib.sha256(secret.encode()).digest()
    h = (
        hashlib.blake2b(raw_token.encode(), key=secretbytes, digest_size=64)
        .digest()
        .hex()
    )
    return h
