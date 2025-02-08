from pydantic import BaseModel, EmailStr

class UserModel(BaseModel):  # ✅ Keep as `UserModel`
    username: str
    email: EmailStr
    password: str  # This should be stored as a hashed password
