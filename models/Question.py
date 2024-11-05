from sqlalchemy import Column, Integer, String, Text, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from config.database import Base


class Question(Base):
    __tablename__ = 'Questions'

    textbook_id = Column(Integer, ForeignKey('Textbook.textbook_id'), primary_key=True)
    chapter_id = Column(String(100), ForeignKey('Chapter.chapter_id'), primary_key=True)
    section_id = Column(String(100), ForeignKey('Section.section_id'), primary_key=True)
    block_id = Column(String(100), ForeignKey('Block.block_id'), primary_key=True)
    unique_activity_id = Column(String(100), ForeignKey('Activity.unique_activity_id'), primary_key=True)
    question_id = Column(String(255), primary_key=True)
    question_text = Column(Text)
    option_1 = Column(Text)
    option_1_explanation = Column(Text)
    option_2 = Column(Text)
    option_2_explanation = Column(Text)
    option_3 = Column(Text)
    option_3_explanation = Column(Text)
    option_4 = Column(Text)
    option_4_explanation = Column(Text)
    answers = Column(Integer)
    hidden = Column(Boolean)

    # Relationships
    activity = relationship("Activity", back_populates="questions")
    supervisions = relationship("CourseSupervision", back_populates="question")