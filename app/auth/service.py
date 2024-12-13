from datetime import timedelta
from sqlalchemy.orm import Session
from app.auth.exceptions import IncorrectUsernameOrPassword
from app.core.database import get_db
from app.core.security import create_access_token, verify_password
from app.models.user import User
from app.config import settings

class AuthService():
    def __init__(self): 
        self.db: Session = get_db()  
    def validate_login(self, email: str, password: str):
        user = self.db.query(User).filter(User.email == email).first()
        
        if not user or not verify_password(password, user.hashed_password):
            raise IncorrectUsernameOrPassword(detail="Incorrect username or password")

        # Create access token
        access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": user.email}, 
            expires_delta=access_token_expires
        )
        
        return {"access_token": access_token, "token_type": "bearer"}