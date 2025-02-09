import logging
from bson import ObjectId
from fastapi import HTTPException
from backend.db.connection import cvs_collection  # ✅ Ensure correct import
logger = logging.getLogger(__name__)

def create_cv(cv_data: dict):
    """Creates a new CV in the database and returns the generated ID."""
    inserted_cv = cvs_collection.insert_one(cv_data)
    
    generated_id = str(inserted_cv.inserted_id)  # ✅ Convert ObjectId to string
    logger.debug(f"Inserted CV ID: {generated_id}")

    return {**cv_data, "id": generated_id}  # ✅ Ensure "id" is a string

def get_cv_by_id(cv_id: str):
    """Retrieves a CV by ID with proper validation."""
    if not ObjectId.is_valid(cv_id):
        raise HTTPException(status_code=400, detail="Invalid CV ID format")

    logger.debug(f"Fetching CV with ID: {cv_id}")
    cv = cvs_collection.find_one({"_id": ObjectId(cv_id)})

    if not cv:
        logger.error(f"CV Not Found: {cv_id}")
        raise HTTPException(status_code=404, detail="CV not found")

    cv["id"] = str(cv["_id"])  # ✅ Convert _id to string
    del cv["_id"]  # ✅ Remove the original _id to avoid conflicts

    return cv  # ✅ Now, the response will contain "id" instead of "_id"

def delete_cv(cv_id: str):
    """Deletes a CV by ID."""
    if not ObjectId.is_valid(cv_id):
        raise HTTPException(status_code=400, detail="Invalid CV ID format")

    result = cvs_collection.delete_one({"_id": ObjectId(cv_id)})

    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="CV not found")

    return {"message": "CV deleted successfully"}
