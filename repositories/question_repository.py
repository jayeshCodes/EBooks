from models import Question
from base_repository import BaseRepository

class QuestionRepository(BaseRepository[Question]):
    def __init__(self, db_session):
        BaseRepository.__init__(self, db_session)