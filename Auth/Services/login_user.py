from Auth.Models.V1.Request.login_user import LoginUserRequest
from Auth.Utils.encrypt import hash_password
from Auth.Utils.jwt_token import encoded_jwt


async def login_user_service(user: LoginUserRequest, algo="HS256"):
    hashed_password = hash_password(user.password)
