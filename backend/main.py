from fastapi import FastAPI
from backend.api.routes.cv import cv_router  
from backend.db.connection import db

app = FastAPI()

# Register routes
app.include_router(cv_router)

@app.get("/")
def read_root():
    return {"message": "CV API is running!"}
