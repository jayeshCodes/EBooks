from base_service import BaseService
from repositories.question_repository import QuestionRepository

class QuestionsService(BaseService):
    def __init__(self, questions_repository : QuestionRepository):
        super().__init__(questions_repository)

    def get_questions_by_activity(self, activity_id):
        return self.repository.get_questions_by_activity(activity_id)