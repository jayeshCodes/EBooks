from models import CourseSupervision
from base_repository import BaseRepository

class CourseSupervisionRepository(BaseRepository[CourseSupervision]):
    def __init__(self, db_session):
        super().__init__(db_session, CourseSupervision)