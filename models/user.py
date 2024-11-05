from sqlalchemy import Column, String, Enum
from sqlalchemy.orm import relationship
from config.database import Base

class User(Base):
    __tablename__ = 'User'

    # Fields
    id = Column(String(255), primary_key=True)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)  # In production, consider hashing passwords!
    role = Column(Enum('Student', 'Faculty', 'TA', 'Admin', name='role_types'), nullable=False)

    # Relationships
    courses_taught = relationship("Course", back_populates="faculty_member", foreign_keys="Course.faculty_member_id")
    ta_courses = relationship("Course", back_populates="ta", foreign_keys="Course.ta_id")
    ta_info = relationship("TAInformation", back_populates="ta")
    enrollments = relationship("Enrollment", back_populates="student")
    scores = relationship("Score", back_populates="student")

    def __repr__(self):
        return f"<User(id='{self.id}', email='{self.email}', role='{self.role}')>"

    def is_admin(self):
        return self.role == 'Admin'

    def is_faculty(self):
        return self.role == 'Faculty'

    def is_student(self):
        return self.role == 'Student'

    def is_ta(self):
        return self.role == 'TA'