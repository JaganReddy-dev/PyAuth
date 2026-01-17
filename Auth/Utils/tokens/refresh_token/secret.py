import secrets
from dotenv import load_dotenv, set_key
from pathlib import Path


def create_secret(algo: str = "HS256") -> dict:
    secret = secrets.token_hex(34)
    BASE_DIR = Path(__file__).resolve().parents[2]
    ENV_PATH = BASE_DIR / ".env"
    load_dotenv(dotenv_path=ENV_PATH, override=True)
    env_path = str(ENV_PATH)
    set_key(env_path, "SECRET", secret)
    set_key(env_path, "ALGORITHM", algo)
    return {"message": "Secret and Algo set at {env_path}"}
