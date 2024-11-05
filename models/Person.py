from sqlalchemy import Column, String, Enum
from sqlalchemy.orm import relationship
from config.database import Base


class Person(Base):
    __tablename__ = 'Person'

    id = Column(String(255), primary_key=True)
    first_name = Column(String(255))
    last_name = Column(String(255))
    email = Column(String(255))
    password = Column(String(255))
    role = Column(Enum('Student', 'Faculty', 'TA', 'Admin', name='role_types'), nullable=False)

    # Relationships
    courses_taught = relationship("Course", back_populates="faculty_member", foreign_keys="Course.faculty_member_id")
    ta_courses = relationship("Course", back_populates="ta", foreign_keys="Course.ta_id")
    ta_info = relationship("TAInformation", back_populates="ta")
    enrollments = relationship("Enrollment", back_populates="student")
    scores = relationship("Score", back_populates="student")