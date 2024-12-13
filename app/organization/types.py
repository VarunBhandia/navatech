from pydantic import BaseModel, EmailStr, Field

class OrganizationCreate(BaseModel):
    email: EmailStr = Field(..., description="Admin email")
    password: str = Field(..., min_length=8, description="Admin password")
    organization_name: str = Field(..., min_length=3, max_length=50)

class OrganizationResponse(BaseModel):
    organization_name: str
    admin_email: str