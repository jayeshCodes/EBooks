from models import Person
from base_repository import BaseRepository

class PersonRepository(BaseRepository[Person]):
    def __init__(self, db_session):
        super().__init__(db_session, Person)