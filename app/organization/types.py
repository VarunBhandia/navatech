from pydantic import BaseModel, Field

class OrganizationCreate(BaseModel):
    email: str = Field(..., description="Admin email")
    password: str = Field(..., min_length=8, description="Admin password")
    organization_name: str = Field(..., min_length=3, max_length=50)

class OrganizationResponse(BaseModel):
    organization_name: str
    admin_email: str