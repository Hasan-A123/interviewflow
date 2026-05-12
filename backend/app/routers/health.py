# routers/health.py

from fastapi import APIRouter

# This creates a router object that groups endpoints together
router = APIRouter()

@router.get("/health")
def health_check():
    return {"status": "healthy"}