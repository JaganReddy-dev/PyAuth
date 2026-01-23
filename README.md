# PyAuth Playground

A FastAPI-based authentication service providing JWT and refresh token management.

## Overview

PyAuth is an authentication and authorization package for user identity management, built with FastAPI. It provides secure token generation, verification, and refresh capabilities.

## Features

- **JWT Token Management**: Create and verify JWT tokens with configurable expiration
- **Refresh Token System**: Secure refresh token generation with hashing
- **Token Verification**: Validate JWT tokens with proper error handling
- **Token Revocation**: Revoke refresh tokens when needed
- **Password Hashing**: Argon2id password hashing utility

## Project Structure

```
pyauth/
├── Auth/
│   ├── Apis/
│   │   └── V1/
│   │       └── tokens.py          # Token API endpoints
│   ├── Models/
│   │   └── V1/
│   │       ├── Request/            # Request models
│   │       │   ├── jwt_gen.py
│   │       │   ├── refresh_rt.py
│   │       │   └── verify_token.py
│   │       └── Response/           # Response models
│   │           ├── error_response.py
│   │           └── verify_token_respose.py
│   ├── Services/
│   │   └── V1/
│   │       └── token_service.py    # Token business logic
│   └── Utils/
│       ├── password_hasher.py      # Argon2 password hashing
│       ├── secret.py               # Environment variable management
│       ├── utc_now.py              # UTC time utility
│       └── tokens/
│           ├── jwt_token.py        # JWT encoding/decoding
│           └── refresh_token/
│               ├── raw_refresh_token.py
│               └── refresh_token_hash.py
├── main.py                         # FastAPI application entry point
├── bootstrap.py                    # Environment setup
└── pyproject.toml                  # Project dependencies
```

## API Endpoints

### POST `/tokens/create`

Create new JWT and refresh tokens.

**Request Body:**

```json
{
  "sub": "user_id"
}
```

**Response:**

```json
{
  "jwt_token": {
    "token": "eyJhbGci...",
    "sub": "user_id",
    "iss": "localhost",
    "aud": "user",
    "iat": 1234567890,
    "exp": 1234567890
  },
  "refresh_token": {
    "id": "uuid",
    "user_id": "user_id",
    "token": "hashed_token",
    "created_at": 1234567890,
    "expiry": 1234567890,
    "revoked": false
  }
}
```

### POST `/tokens/verify`

Verify a JWT token.

**Request Body:**

```json
{
  "token": "eyJhbGci..."
}
```

**Response:**

```json
{
  "sub": "user_id",
  "iss": "localhost",
  "aud": "user"
}
```

**Error Responses:**

- `401 Unauthorized`: Invalid or expired token

### POST `/tokens/refresh`

Refresh JWT and refresh tokens using an existing refresh token.

**Request Body:**

```json
{
  "id": "uuid",
  "user_id": "user_id",
  "token": "hashed_token",
  "created_at": 1234567890,
  "expiry": 1234567890,
  "revoked": false
}
```

**Response:**

```json
{
  "revoked_rt": {...},
  "jwt_token": {...},
  "refresh_token": {...}
}
```

### DELETE `/tokens/revoke`

Revoke a refresh token.

**Request Body:**

```json
{
  "id": "uuid",
  "user_id": "user_id",
  "token": "hashed_token",
  "created_at": 1234567890,
  "expiry": 1234567890,
  "revoked": false
}
```

**Response:**

```json
{
  "id": "uuid",
  "user_id": "user_id",
  "token": "hashed_token",
  "created_at": 1234567890,
  "expiry": 1234567890,
  "revoked": true
}
```

## Environment Variables

The following environment variables are required (configured via `.env` file):

- `SECRET`: Secret key for JWT signing
- `ALGORITHM`: JWT algorithm (e.g., "HS256")
- `REFRESH_TOKEN_SECRET`: Secret for refresh token hashing
- `REFRESH_TOKEN_EXPIRE_DAYS`: Number of days until refresh token expires

## Dependencies

- **FastAPI**: Web framework
- **PyJWT**: JWT token handling
- **Argon2-cffi**: Password hashing
- **Cryptography**: Cryptographic primitives
- **Pydantic**: Data validation
- **Python-dotenv**: Environment variable management
- **Uvicorn**: ASGI server

## Installation

1. Install dependencies:

```bash
uv sync
```

2. Create a `.env` file with required environment variables:

```
SECRET=your-secret-key
ALGORITHM=HS256
REFRESH_TOKEN_SECRET=your-refresh-token-secret
REFRESH_TOKEN_EXPIRE_DAYS=30
```

3. Run the application:

```bash
uvicorn main:app --reload
```

## Token Configuration

- **JWT Token Expiration**: 5 minutes (hardcoded)
- **Refresh Token Expiration**: Configurable via `REFRESH_TOKEN_EXPIRE_DAYS` environment variable
- **JWT Claims**:
  - `sub`: Subject (user ID)
  - `iss`: Issuer (localhost)
  - `aud`: Audience (user)
  - `iat`: Issued at
  - `exp`: Expiration time

## Utilities

### Password Hashing

The `password_hasher.py` module provides Argon2id password hashing with:

- Time cost: 5 iterations
- Memory cost: 7168 KiB (7 MiB)
- Parallelism: 1 thread

### Secret Management

The `secret.py` module handles environment variable retrieval with validation, ensuring required secrets are present at runtime.
