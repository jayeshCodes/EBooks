from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from config.database import Base


class TAInformation(Base):
    __tablename__ = 'TAInformation'

    ta_id = Column(String(255), ForeignKey('Person.id'), primary_key=True)
    course_id = Column(String(255), ForeignKey('Course.unique_course_id'))
    faculty_id = Column(String(255), ForeignKey('Person.id'))

    # Relationships
    ta = relationship("Person", back_populates="ta_info", foreign_keys=[ta_id])
    faculty = relationship("Person", foreign_keys=[faculty_id])
    course = relationship("Course")