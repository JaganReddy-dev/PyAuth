import os
import dotenv

dotenv.load_dotenv()

def get_required_secret(name: str) -> str:
    name = name.strip()
    if not name:
        raise ValueError("Environment variable name cannot be empty")

    value = os.getenv(name)
    if value is None:
        raise RuntimeError(
            f"Missing required environment variable: {name}"
        )
    return value