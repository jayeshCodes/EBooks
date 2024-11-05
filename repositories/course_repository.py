from models import Course
from base_repository import BaseRepository

class CourseRepository(BaseRepository[Course]):
    def __init__(self, db_session):
        super().__init__(db_session, Course)