import jwt
import dotenv

dotenv.load_dotenv()

def encoded_jwt(payload, secret, algorithm):
    return jwt.encode(payload, secret, algorithm)


def decoded_jwt(token, secret, algorithm, aud):
    return jwt.decode(token, secret, algorithm, audience=aud)
