import pytest
from backend.services.auth_service import hash_password, verify_password, create_jwt_token, decode_jwt_token

def test_hash_password():
    """Test password hashing."""
    password = "securepass"
    hashed_password = hash_password(password)
    assert hashed_password != password  # Should not be the same
    assert verify_password(password, hashed_password) == True

def test_jwt_token():
    """Test JWT token generation and decoding."""
    user_id = "123"
    token = create_jwt_token(user_id)
    decoded_data = decode_jwt_token(token)
    assert decoded_data["user_id"] == user_id
