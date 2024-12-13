from datetime import timedelta
from sqlalchemy.orm import Session
from app.auth.exceptions import IncorrectUsernameOrPassword
from app.core.database import get_db
from app.core.security import create_access_token, verify_password
from app.config import settings
from app.user.model import User

class AuthService():
    def __init__(self): 
        gen = get_db()
        self.db: Session = next(gen)
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
        
        return access_token