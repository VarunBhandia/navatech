from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from app.auth.service import AuthService

router = APIRouter()

@router.post("/login")
def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends()):

    auth_service = AuthService()
    access_token = auth_service.validate_login(form_data.username, form_data.password)    
    return {"access_token": access_token, "token_type": "bearer"}