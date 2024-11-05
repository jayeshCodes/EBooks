from sqlalchemy import Column, String, Integer, Date, Enum, ForeignKey
from sqlalchemy.orm import relationship
from config.database import Base


class Course(Base):
    __tablename__ = 'Course'

    unique_course_id = Column(String(255), primary_key=True)
    course_name = Column(String(255))
    unique_e_textbook_id = Column(Integer, ForeignKey('Textbook.textbook_id'))
    course_type = Column(Enum('Active', 'Evaluation', name='course_types'), nullable=False)
    faculty_member_id = Column(String(255), ForeignKey('Person.id'))
    ta_id = Column(String(255), ForeignKey('Person.id'))
    course_start_date = Column(Date)
    course_end_date = Column(Date)
    unique_token = Column(String(255))
    course_capacity = Column(Integer)

    # Relationships
    textbook = relationship("Textbook", back_populates="courses")
    faculty_member = relationship("Person", back_populates="courses_taught", foreign_keys=([faculty_member_id]).__str__())
    ta = relationship("Person", back_populates="ta_courses", foreign_keys=([ta_id]).__str__())
    enrollments = relationship("Enrollment", back_populates="course")
    scores = relationship("Score", back_populates="course")
