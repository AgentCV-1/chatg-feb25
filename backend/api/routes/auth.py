from fastapi import APIRouter, HTTPException
from backend.db.models.user import UserModel  
from backend.db.connection import db  
from backend.services.auth_service import hash_password, verify_password, create_jwt_token  # ✅ Fixed import

auth_router = APIRouter()
user_collection = db["users"]

@auth_router.post("/register/")
def register_user(user: UserModel):
    if user_collection.find_one({"email": user.email}):
        raise HTTPException(status_code=400, detail="User already exists")

    user.password = hash_password(user.password)
    user_collection.insert_one(user.dict())
    return {"message": "User registered successfully"}

@auth_router.post("/login/")
def login_user(user: UserModel):
    db_user = user_collection.find_one({"email": user.email})
    if not db_user or not verify_password(user.password, db_user["password"]):
        raise HTTPException(status_code=400, detail="Invalid credentials")

    token = create_jwt_token(str(db_user["_id"]))
    return {"access_token": token}
