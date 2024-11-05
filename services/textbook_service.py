from base_service import BaseService
from repositories.textbook_repository import TextbookRepository

class TextbookService(BaseService):
    def __init__(self, textbook_repository : TextbookRepository):
        super().__init__(textbook_repository)