from models import Activity
from base_repository import BaseRepository

class ActivityRepository(BaseRepository[Activity]):
    def __init__(self, db_session):
        super().__init__(db_session, Activity)