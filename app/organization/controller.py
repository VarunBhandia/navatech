from fastapi import APIRouter
from app.organization.exceptions import OrganizationAlreadyExists, OrganizationNotFound
from app.organization.service import OrganizationService
from app.organization.types import OrganizationCreate, OrganizationResponse
from fastapi.exceptions import HTTPException

router = APIRouter()

@router.post("", response_model=OrganizationResponse)
def create_organization(
    org_data: OrganizationCreate, 
):
    try:
        organization_service = OrganizationService()
        new_org = organization_service.create_organization_with_user(org_data)
        return OrganizationResponse(
            organization_name=new_org.name,
            admin_email=new_org.admin_email
        ) 
    except OrganizationAlreadyExists as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("", response_model=OrganizationResponse)
def get_organization(
    organization_name: str, 
):
    try:
        organization_service = OrganizationService()

        org = organization_service.get_organization(organization_name)
        
        return OrganizationResponse(
            organization_name=org.name,
            admin_email=org.admin_email
        )
    except OrganizationNotFound as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))