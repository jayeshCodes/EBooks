from base_service import BaseService
from repositories.chapter_repository import ChapterRepository

class ChapterService(BaseService):
    def __init__(self, chapter_repository: ChapterRepository):
        super().__init__(chapter_repository)