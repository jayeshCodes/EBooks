from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from config.database import Base


class Activity(Base):
    __tablename__ = 'Activity'

    textbook_id = Column(Integer, ForeignKey('Textbook.textbook_id'), primary_key=True)
    chapter_id = Column(String(100), ForeignKey('Chapter.chapter_id'), primary_key=True)
    section_id = Column(String(100), ForeignKey('Section.section_id'), primary_key=True)
    block_id = Column(String(100), ForeignKey('Block.block_id'), primary_key=True)
    unique_activity_id = Column(String(100), primary_key=True)
    hidden = Column(Boolean)

    # Relationships
    block = relationship("Block", back_populates="activities")
    questions = relationship("Question", back_populates="activity")
    supervisions = relationship("CourseSupervision", back_populates="activity")
