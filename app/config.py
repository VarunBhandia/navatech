from pydantic_settings import BaseSettings
import os

class Settings(BaseSettings):
    SECRET_KEY: str = os.getenv('SECRET_KEY', 'your-secret-key')
    ALGORITHM: str = 'HS256'
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # Master Database Configuration
    MASTER_DB_URL: str = os.getenv('MASTER_DB_URL', 'sqlite:///./master.db')
    
    class Config:
        env_file = '.env'

settings = Settings()
