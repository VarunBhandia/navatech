from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sqlite3
import os
from datetime import datetime
from app.config import settings
# Master Database Engine
master_engine = create_engine(settings.MASTER_DB_URL)
MasterSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=master_engine)

# Base class for SQLAlchemy models
Base = declarative_base()

class OrganizationDatabase(Base):
    """
    Model to store dynamic database information in the master database
    """
    __tablename__ = "organization_databases"
    
    id = Column(Integer, primary_key=True, index=True)
    org_name = Column(String, unique=True, index=True)
    db_path = Column(String, unique=True)
    created_at = Column(DateTime, default=datetime.utcnow)

def create_dynamic_database(org_name: str):
    """
    Create a dynamic SQLite database for a specific organization
    """
    os.makedirs('organization_databases', exist_ok=True)
    
    db_path = f'organization_databases/{org_name}_database.db'
    
    conn = sqlite3.connect(db_path)
    conn.close()
    
    db = MasterSessionLocal()
    try:
        org_db = OrganizationDatabase(
            org_name=org_name,
            db_path=db_path
        )
        db.add(org_db)
        db.commit()
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()
    
    return db_path

def get_organization_database(org_name: str):
    """
    Retrieve the database path for a specific organization
    """
    db = MasterSessionLocal()
    try:
        org_db = db.query(OrganizationDatabase).filter(OrganizationDatabase.org_name == org_name).first()
        if not org_db:
            raise ValueError(f"No database found for organization: {org_name}")
        return org_db.db_path
    finally:
        db.close()

def get_db():
    """
    Database session generator for master database
    """
    db = MasterSessionLocal()
    Base.metadata.create_all(bind=master_engine)
    try:
        yield db
    finally:
        db.close()