from fastapi import FastAPI, Request
from fastapi.middleware.trustedhost import TrustedHostMiddleware  # ✅ Correct import
from backend.api.routes.cv import cv_router
from backend.api.routes.auth import auth_router
import logging
import uvicorn

# ✅ Define the FastAPI app
app = FastAPI()

# ✅ Logging setup
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# ✅ Middleware to log requests (Using Custom Middleware)
class LogRequestsMiddleware:
    async def __call__(self, request: Request, call_next):
        logger.debug(f"Incoming Request: {request.method} {request.url}")
        response = await call_next(request)
        logger.debug(f"Response Status: {response.status_code}")
        return response

# ✅ Register Middleware (TrustedHost & Logging Middleware)
app.add_middleware(TrustedHostMiddleware, allowed_hosts=["*"])  # Protect against Host header attacks

# ✅ Register API routes
app.include_router(cv_router)
app.include_router(auth_router)

@app.get("/")
def health_check():
    logger.debug("Health check endpoint hit")  # ✅ Log when API starts
    return {"message": "API is running!"}

# ✅ Ensure the script runs when executed directly
if __name__ == "__main__":
    logger.debug("Starting FastAPI server...")
    uvicorn.run("backend.main:app", host="127.0.0.1", port=8000, reload=True)
