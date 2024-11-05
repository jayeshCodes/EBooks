from models import Chapter
from base_repository import BaseRepository

class ChapterRepository(BaseRepository[Chapter]):
    def __init__(self, db_session):
        super().__init__(db_session, Chapter)