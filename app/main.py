from fastapi import FastAPI
from app.organization import controller

app = FastAPI(
    title="Organization Management API",
    description="API for managing organizations with dynamic database creation",
    version="0.1.0"
)

# Include routers
app.include_router(
    controller.router, 
    prefix="/org", 
    tags=["Organization Management"]
)

@app.get("/")
def read_root():
    """
    Health check endpoint
    """
    return {"status": "healthy"}