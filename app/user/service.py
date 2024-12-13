from app.core.database import get_db
from app.core.security import get_password_hash
from sqlalchemy.orm import Session

from app.user.model import User


class UserService():

    def __init__(self): 
        gen = get_db()
        self.db: Session = next(gen)

    def create_user(self, email: str, password: str, org_id: int) -> User:
        hashed_password = get_password_hash(password)
        created_user = User(
            email=email,
            hashed_password=hashed_password,
            org_id=org_id
        )
        self.db.add(created_user)
        self.db.commit()
        self.db.refresh(created_user)

        return created_user
        