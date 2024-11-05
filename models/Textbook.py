from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from config.database import Base


class Textbook(Base):
    __tablename__ = 'Textbook'

    textbook_id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)

    # Relationships
    courses = relationship("Course", back_populates="textbook")
    chapters = relationship("Chapter", back_populates="textbook")