import hashlib
from Auth.Utils.secret import get_required_secret


def create_refresh_token_hash(token: str) -> bytes:
    secret = get_required_secret("REFRESH_TOKEN_SECRET")
    secretbytes = hashlib.sha256(secret.encode()).digest()
    h = hashlib.blake2b(token.encode(), key=secretbytes, digest_size=64).digest().hex()
    return h
