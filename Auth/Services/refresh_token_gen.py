from datetime import datetime, timedelta, timezone
from Auth.Utils.tokens.refresh_token.refresh_token import create_refresh_token
import uuid
import os


def create_whole_refresh_token(user_id):
    token = create_refresh_token()
    id = str(uuid.uuid4())
    now = datetime.now(timezone.utc)
    refresh_token_expiry = int(os.getenv("REFRESH_TOKEN_EXPIRE_DAYS", "8"))
    created_at = now
    expiry = now + timedelta(days=refresh_token_expiry)
    revoked = False
    document = {
        "id": id,
        "user_id": user_id,
        "token": token["hashed_token"],
        "created_at": created_at,
        "expiry": expiry,
        "revoked": revoked,
    }
    return document
