from fastapi import APIRouter, HTTPException
from backend.services.cv_service import create_cv, get_cv_by_id, delete_cv
from backend.db.models.cv import CVModel

cv_router = APIRouter()

@cv_router.post("/cv/", response_model=CVModel)
def create_cv_route(cv: CVModel):
    """Create a new CV in the database"""
    return create_cv(cv.dict())

@cv_router.get("/cv/{cv_id}", response_model=CVModel)
def get_cv_route(cv_id: str):
    """Retrieve a CV by ID"""
    return get_cv_by_id(cv_id)

@cv_router.delete("/cv/{cv_id}")
def delete_cv_route(cv_id: str):
    """Delete a CV by ID"""
    return delete_cv(cv_id)
