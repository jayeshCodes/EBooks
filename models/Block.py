from sqlalchemy import Column, Integer, String, Text, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from config.database import Base


class Block(Base):
    __tablename__ = 'Blocks'

    textbook_id = Column(Integer, ForeignKey('Textbook.textbook_id'), primary_key=True)
    chapter_id = Column(String(100), ForeignKey('Chapter.chapter_id'), primary_key=True)
    section_id = Column(String(100), ForeignKey('Section.section_id'), primary_key=True)
    block_id = Column(String(100), primary_key=True)
    type = Column(String(255))
    content = Column(Text)
    hidden = Column(Boolean)
    created_by = Column(String(255), ForeignKey('Person.id'))

    # Relationships
    section = relationship("Section", back_populates="blocks")
    activities = relationship("Activity", back_populates="block")