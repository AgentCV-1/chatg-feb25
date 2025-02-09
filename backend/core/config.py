import os
from dotenv import load_dotenv

# ✅ Get absolute path to `.env` file
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
ENV_PATH = os.path.join(BASE_DIR, ".env")

# ✅ Load environment variables explicitly
load_dotenv(dotenv_path=ENV_PATH, override=True)

# ✅ Ensure SECRET_KEY is loaded
SECRET_KEY = os.getenv("SECRET_KEY")

if not SECRET_KEY:
    raise ValueError("❌ SECRET_KEY is missing! Check your .env file.")

print(f"✅ Loaded SECRET_KEY: {SECRET_KEY[:5]}*****")  # ✅ Debugging (Prints only first 5 characters)
