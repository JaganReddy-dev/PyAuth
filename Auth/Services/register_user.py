from Auth.Models.V1.Request.register_user import RegisterUserRequest
from Auth.Utils.encrypt import hash_password
import uuid
from Auth.Utils.utc_now import utc_now


async def resgister_user_service(user: RegisterUserRequest):
    new_uuid = uuid.uuid4()
    now = utc_now()
    user_dict = user.model_dump()
    user_dict["id"] = str(new_uuid)
    user_dict["created_at"] = now
    user_dict["updated_at"] = now
    user_dict["password_hash"] = hash_password(user_dict["password"])
    user_dict["email"] = str(user_dict["email"])
    user_dict["verified"] = False

    return user_dict
