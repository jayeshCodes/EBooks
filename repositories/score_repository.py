from models.Score import Score
from base_repository import BaseRepository

class ScoreRepository(BaseRepository):
    def __init__(self, db_session):
        super().__init__(db_session, Score)