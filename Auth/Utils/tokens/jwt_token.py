import jwt


def encoded_jwt(payload, secret, algorithm):
    return jwt.encode(payload, secret, algorithm)


def decoded_jwt(token, secret, algorithm):
    return jwt.decode(token, secret, algorithm)
