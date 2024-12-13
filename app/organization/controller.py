from fastapi import APIRouter
from app.organization.service import OrganizationService
from app.organization.types import OrganizationCreate, OrganizationResponse

router = APIRouter()

@router.post("/", response_model=OrganizationResponse)
def create_organization(
    org_data: OrganizationCreate, 
):
    
    organization_service = OrganizationService()
    new_org = organization_service.create_organization_with_user(org_data)
    return OrganizationResponse(
        organization_name=new_org.name,
        admin_email=new_org.admin_email
    )

@router.get("/", response_model=OrganizationResponse)
def get_organization(
    organization_name: str, 
):
    organization_service = OrganizationService()

    org = organization_service.get_organization(organization_name)
    
    return OrganizationResponse(
        organization_name=org.name,
        admin_email=org.admin_email
    )