import bcrypt
import jwt
import logging
from datetime import datetime, timedelta
from backend.core.config import SECRET_KEY  # ✅ Import from config.py

# ✅ Hash password function
def hash_password(password: str) -> str:
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode(), salt).decode()

# ✅ Verify password function
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(plain_password.encode(), hashed_password.encode())

# ✅ Create JWT Token
def create_jwt_token(user_id: str) -> str:
    payload = {"user_id": user_id, "exp": datetime.utcnow() + timedelta(days=7)}
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

# ✅ Decode JWT Token
def decode_jwt_token(token: str):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        return None
