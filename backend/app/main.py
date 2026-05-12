from fastapi import FastAPI
from app.routers import health
from app.db.database import Base, engine
from app.models import user
from app.routers.health import router as health_router

# Create the FastAPI application instance with metadata
app = FastAPI(
    title="InterviewFlow API",
    description="A technical interview practice platform",
    version="1.0.0"
)

app.include_router(health_router)

# Event that runs when the application starts
@app.on_event("startup")
def on_startup():
    # Create all database tables defined in SQLAlchemy models
    Base.metadata.create_all(bind=engine)

# Include the health check router
app.include_router(health.router)

# Root endpoint for basic API status
@app.get("/")
def root():
    return {"message": "InterviewFlow API is running"}

# Simple health status endpoint
@app.get("/Health")
def health_status():
    return {"status": "ok"}
