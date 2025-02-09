from pymongo import MongoClient
import os
from dotenv import load_dotenv

# ✅ Load environment variables
load_dotenv()

# ✅ Get MongoDB URI from .env file (fallback to local MongoDB if not found)
DATABASE_URL = os.getenv("MONGO_URI", "mongodb://localhost:27017/")

# ✅ Connect to MongoDB
client = MongoClient(DATABASE_URL)

# ✅ Define the database
db = client["cv_database"]  # Ensure this matches your database name

# ✅ Define collections (equivalent to tables in SQL)
users_collection = db["users"]
cvs_collection = db["cvs"]  # ✅ Ensure this line exists
