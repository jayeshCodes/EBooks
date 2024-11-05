from models import Textbook
from base_repository import BaseRepository

class TextbookRepository(BaseRepository[Textbook]):
    def __init__(self, db_session):
        super().__init__(db_session, Textbook)