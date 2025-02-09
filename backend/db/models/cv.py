from typing import List, Optional
from backend.db.connection import db
from backend.services.auth_service import hash_password
from pydantic import BaseModel, Field
from typing import List

class CVModel(BaseModel):
    user_id: str
    name: str
    email: str
    phone: str
    experience: List[str]  # ✅ Ensure list type is correct
    education: List[str]  # ✅ Ensure list type is correct
    skills: List[str]  # ✅ Ensure list type is correct
    summary: str
    id: str = Field(None, alias="id")  # ✅ Make "id" optional

    class Config:
        populate_by_name = True
        from_attributes = True  # ✅ Allow conversion from MongoDB documents
