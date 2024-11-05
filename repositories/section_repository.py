from models import Section
from base_repository import BaseRepository

class SectionRepository(BaseRepository[Section]):
    def __init__(self, db_session):
        super().__init__(db_session, Section)