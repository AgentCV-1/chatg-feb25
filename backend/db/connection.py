from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get MongoDB URI from .env file
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")

# Connect to MongoDB
client = MongoClient(MONGO_URI)

# Define the database
db = client["cv_database"]

# Collections (Tables in SQL terms)
users_collection = db["users"]
cvs_collection = db["cvs"]
