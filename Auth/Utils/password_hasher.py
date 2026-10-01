from argon2 import PasswordHasher

ph = PasswordHasher(
    time_cost=5,  # t=5: Number of iterations
    memory_cost=20972,  # m=20972: Memory usage in KiB (20 MiB)
    parallelism=1,  # p=1: Number of parallel threads
)


def hash_password(password):
    """
    Hash a password using Argon2id with custom parameters.
    m=20972 (20 MiB), t=5, p=1

    Args:
        password: Plain text password to hash

    Returns:
        Hashed password as a string

    Example:
        >>> hashed = hash_password("MyPassword123!")
        >>> print(hashed)
        $argon2id$v=19$m=20972,t=5,p=1$...$...
    """
    if not password:
        raise ValueError("Password cannot be empty")

    try:
        hashed = ph.hash(password)
        return hashed
    except Exception as e:
        raise ValueError(f"Error hashing password: {str(e)}")
