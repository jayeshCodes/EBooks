from models import Block
from base_repository import BaseRepository

class BlockRepository(BaseRepository[Block]):
    def __init__(self, db_session):
        super().__init__(db_session, Block)