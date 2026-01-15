import jwt


def encoded_jwt(document, secret, algo):
    return jwt.encode(document, secret, algo)


def decoded_jwt(token, secret, algo):
    return jwt.decode(token, secret, algo)
