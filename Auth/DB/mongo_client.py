from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://eastboundcode:<db_password>@cluster0.rguftoz.mongodb.net/?appName=Cluster0"
client = MongoClient(uri, server_api=ServerApi("1"))

try:
    client.admin.command("ping")
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client["pyauth"]
users = db["users"]
sessions = db["sessions"]
password_reset = db["password_resets"]
passwords = db["passwords"]
jwt_tokens = db["jwt_tokens"]
roles = db["roles"]

db.users.create_index({"email": 1, "username": 1, "uuid": 1}, {"unique": True})
