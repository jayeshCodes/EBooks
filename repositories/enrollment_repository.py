from models import Enrollment
from base_repository import BaseRepository

class EnrollmentRepository(BaseRepository[Enrollment]):
    def __init__(self, db_session):
        super().__init__(db_session, Enrollment)