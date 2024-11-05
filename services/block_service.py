from base_service import BaseService
from repositories.block_repository import BlockRepository

class BlockService(BaseService):
    def __init__(self, block_repository: BlockRepository):
        super().__init__(block_repository)