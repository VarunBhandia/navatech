from fastapi import FastAPI
from app.organization import controller as organization_controller
from app.auth import controller as auth_controller

app = FastAPI(
    title="Organization Management API",
    description="API for managing organizations with dynamic database creation",
    version="0.1.0"
)

# Include routers
app.include_router(
    organization_controller.router, 
    prefix="/org", 
    tags=["Organization Management"]
)

app.include_router(
    auth_controller.router, 
    prefix="/auth", 
    tags=["Auth"]
)

@app.get("/health-check")
def health_check():
    """
    Health check endpoint
    """
    return {"success": True}