class OrganizationAlreadyExists(Exception):
    def __init__(self, organization_name: str,):
        self.organization_name = organization_name
        self.message = f"Organization {organization_name} already exists"
        super().__init__(self.message)



class OrganizationNotFound(Exception):
    def __init__(self, organization_name: str):
        self.organization_name = organization_name
        self.message = f"Organization '{organization_name}' not found"
        super().__init__(self.message)
