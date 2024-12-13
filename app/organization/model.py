from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.core.database import Base

class Organization(Base):
    __tablename__ = "organizations"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, unique=True,index=True)
    admin_email = Column(String, unique=True)
    
    users = relationship("User", back_populates="organization")