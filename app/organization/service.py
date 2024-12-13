
from app.core.database import create_dynamic_database, get_db
from sqlalchemy.orm import Session
from app.organization.exceptions import OrganizationAlreadyExists, OrganizationNotFound
from app.organization.model import Organization
from app.organization.types import OrganizationCreate
from app.user.service import UserService

class OrganizationService:
    def __init__(self): 
        gen = get_db()
        self.db: Session = next(gen)
    
    def create_organization_with_user(self, org_data: OrganizationCreate) -> Organization:
        existing_org = self.db.query(Organization).filter(Organization.name == org_data.organization_name).first()
        if existing_org:
            raise OrganizationAlreadyExists("Organization already exists")
        
        create_dynamic_database(org_data.organization_name)
        
        new_org = Organization(
            name=org_data.organization_name,
            admin_email=org_data.email
        )
        self.db.add(new_org)
        
        self.db.commit()
        self.db.refresh(new_org)

        user_service = UserService()
        user_service.create_user(org_data.email, org_data.password, new_org.id)

        return new_org

    def get_organization(self,organization_name: str):

        org = self.db.query(Organization).filter(Organization.name == organization_name).first()
        if not org:
            raise OrganizationNotFound(organization_name)
        
        return org