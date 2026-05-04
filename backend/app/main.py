# Import FastAPI framework
from fastapi import FastAPI

# Create FastAPi app instance
# This is the main entry point of the backend api
app = FastAPI()

# Health check endpoint
# Used to check if backend is running correctly
@app.get("/")
def read_root():
    return{"message": "InterviewFlow API is running"}

# Another test endpoint
# This helps confirm routing works
@app.get("/health")
def health_check():
    return {"status": "ok"}