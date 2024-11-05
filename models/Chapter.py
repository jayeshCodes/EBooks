from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from config.database import Base


class Chapter(Base):
    __tablename__ = 'Chapter'

    textbook_id = Column(Integer, ForeignKey('Textbook.textbook_id'), primary_key=True)
    chapter_id = Column(String(100), primary_key=True)
    title = Column(String(255), nullable=False)
    hidden = Column(Boolean)
    created_by = Column(String(255), ForeignKey('Person.id'))

    # Relationships
    textbook = relationship("Textbook", back_populates="chapters")
    sections = relationship("Section", back_populates="chapter")
