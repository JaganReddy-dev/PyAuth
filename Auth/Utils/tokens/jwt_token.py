import jwt
import dotenv

dotenv.load_dotenv()


def encoded_jwt(payload, secret, algorithm):
    required_fields = {
        "payload": payload,
        "secret": secret,
        "algorithm": algorithm,
    }
    missing = [name for name, value in required_fields.items() if not value]
    if missing:
        raise ValueError(f"Missing required field(s): {', '.join(missing)}")

    return jwt.encode(payload, secret, algorithm)


def decoded_jwt(token, secret, algorithm, aud):
    required_fields = {
        "token": token,
        "secret": secret,
        "algorithm": algorithm,
        "audience": aud,
    }
    missing = [name for name, value in required_fields.items() if not value]
    if missing:
        raise ValueError(f"Missing required field(s): {', '.join(missing)}")
    return jwt.decode(token, secret, algorithm, audience=aud)
