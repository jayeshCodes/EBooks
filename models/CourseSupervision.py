from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from config.database import Base


class CourseSupervision(Base):
    __tablename__ = 'CourseSupervision'

    student_id = Column(String(100), ForeignKey('Person.id'), primary_key=True)
    course_id = Column(String(100), ForeignKey('Course.unique_course_id'), primary_key=True)
    textbook_id = Column(Integer, ForeignKey('Textbook.textbook_id'), primary_key=True)
    chapter_id = Column(String(100), ForeignKey('Chapter.chapter_id'), primary_key=True)
    section_id = Column(String(100), ForeignKey('Section.section_id'), primary_key=True)
    block_id = Column(String(100), ForeignKey('Block.block_id'), primary_key=True)
    unique_activity_id = Column(String(100), ForeignKey('Activity.unique_activity_id'), primary_key=True)
    question_id = Column(String(100), ForeignKey('Questions.question_id'), primary_key=True)
    point = Column(Integer)
    timestamp = Column(DateTime)

    # Relationships
    student = relationship("Person")
    course = relationship("Course")
    activity = relationship("Activity", back_populates="supervisions")
    question = relationship("Question", back_populates="supervisions")