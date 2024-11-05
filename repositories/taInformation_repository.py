from models import TAInformation
from base_repository import BaseRepository

class TAInformationRepository(BaseRepository[TAInformation]):
    def __init__(self, db_session):
        super().__init__(db_session, TAInformation)