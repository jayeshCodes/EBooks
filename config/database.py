"""imports"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.pool import QueuePool
from datetime import datetime, timezone
from sqlalchemy import Column, DateTime

from config.constants import db_url

# DB config
# DB_CONFIG = {
#     'host' : host,
#     'port' : port,
#     'database' : db_name,
#     'user' : user,
#     'password' : password
# }

# Create database url
DATABASE_URL = db_url

# Create engine with connection pooling
engine = create_engine(
    DATABASE_URL,
    poolclass=QueuePool,
    pool_size=5,
    max_overflow=10,
    pool_timeout=30,
    pool_recycle=3600
)

# Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create declarative base for models
Base = declarative_base()


# Database dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Base repository class
class BaseRepository:
    def __init__(self, db_session):
        self.db = db_session

    def commit(self):
        try:
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            raise e


# Example model base class
class BaseModel(Base):
    __abstract__ = True

    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))


    updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc),
                        onupdate=lambda: datetime.now(timezone.utc))