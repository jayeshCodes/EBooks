from sqlalchemy import Column, String, Enum, ForeignKey
from sqlalchemy.orm import relationship
from config.database import Base


class Enrollment(Base):
    __tablename__ = 'Enrollment'

    unique_course_id = Column(String(255), ForeignKey('Course.unique_course_id'), primary_key=True)
    student_id = Column(String(255), ForeignKey('Person.id'), primary_key=True)
    status = Column(Enum('Enrolled', 'Pending', name='enrollment_status'), nullable=False)

    # Relationships
    course = relationship("Course", back_populates="enrollments")
    student = relationship("Person", back_populates="enrollments")
