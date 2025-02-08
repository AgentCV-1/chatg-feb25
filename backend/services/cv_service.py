import logging
from backend.db.connection import db
from backend.db.models.cv import CVModel
from bson import ObjectId
from fastapi import HTTPException

logger = logging.getLogger(__name__)  # Logging for debugging

cvs_collection = db["cvs"]  # Ensure correct collection name

def create_cv(cv_data: dict):
    """Creates a new CV in the database."""
    inserted_cv = cvs_collection.insert_one(cv_data)
    return {**cv_data, "id": str(inserted_cv.inserted_id)}

def get_cv_by_id(cv_id: str):
    """Retrieves a CV by ID with proper validation."""
    if not ObjectId.is_valid(cv_id):
        raise HTTPException(status_code=400, detail="Invalid CV ID format")
    
    logger.debug(f"Fetching CV with ID: {cv_id}")
    cv = cvs_collection.find_one({"_id": ObjectId(cv_id)})
    
    if not cv:
        logger.error(f"CV Not Found: {cv_id}")
        raise HTTPException(status_code=404, detail="CV not found")

    cv["id"] = str(cv["_id"])
    del cv["_id"]
    return cv

def delete_cv(cv_id: str):
    """Deletes a CV by ID."""
    if not ObjectId.is_valid(cv_id):
        raise HTTPException(status_code=400, detail="Invalid CV ID format")

    result = cvs_collection.delete_one({"_id": ObjectId(cv_id)})

    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="CV not found")

    return {"message": "CV deleted successfully"}
