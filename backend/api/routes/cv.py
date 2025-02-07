from fastapi import APIRouter, HTTPException, Depends
from backend.db.models.cv import CVModel
from backend.db.connection import cvs_collection
from bson import ObjectId
from typing import List

cv_router = APIRouter()

@cv_router.post("/cv/", response_model=CVModel)
def create_cv(cv: CVModel):
    """Create a new CV in the database"""
    cv_dict = cv.dict()
    result = cvs_collection.insert_one(cv_dict)
    return {**cv_dict, "id": str(result.inserted_id)}

@cv_router.get("/cv/{cv_id}", response_model=CVModel)
def get_cv(cv_id: str):
    """Retrieve a CV by ID"""
    cv = cvs_collection.find_one({"_id": ObjectId(cv_id)})
    if not cv:
        raise HTTPException(status_code=404, detail="CV not found")
    cv["id"] = str(cv["_id"])
    return cv

@cv_router.delete("/cv/{cv_id}")
def delete_cv(cv_id: str):
    """Delete a CV by ID"""
    result = cvs_collection.delete_one({"_id": ObjectId(cv_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="CV not found")
    return {"message": "CV deleted successfully"}
