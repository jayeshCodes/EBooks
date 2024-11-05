from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from config.database import Base


class Score(Base):
    __tablename__ = 'Score'

    student_id = Column(String(255), ForeignKey('Person.id'), primary_key=True)
    registered_course_id = Column(String(255), ForeignKey('Course.unique_course_id'), primary_key=True)
    total_participation_points = Column(Integer)
    number_of_finished_activities = Column(Integer)

    # Relationships
    student = relationship("Person", back_populates="scores")
    course = relationship("Course", back_populates="scores")