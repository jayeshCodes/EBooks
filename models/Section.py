from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from config.database import Base


class Section(Base):
    __tablename__ = 'Sections'

    textbook_id = Column(Integer, ForeignKey('Textbook.textbook_id'), primary_key=True)
    chapter_id = Column(String(100), ForeignKey('Chapter.chapter_id'), primary_key=True)
    section_id = Column(String(100), primary_key=True)
    title = Column(String(255), nullable=False)
    hidden = Column(Boolean)
    created_by = Column(String(255), ForeignKey('Person.id'))

    # Relationships
    chapter = relationship("Chapter", back_populates="sections")
    blocks = relationship("Block", back_populates="section")
