from pydantic import BaseModel
from typing import List, Optional
from backend.db.connection import db
from backend.services.auth_service import hash_password


class CVModel(BaseModel):
    user_id: str
    name: str
    email: str
    phone: str
    experience: List[str]
    education: List[str]
    skills: List[str]
    summary: Optional[str] = None
