from base_service import BaseService
from repositories.score_repository import ScoreRepository

class ScoreService(BaseService):
    def __init__(self, score_repository : ScoreRepository):
        super().__init__(score_repository)

    def get_scores_by_student(self, student_id):
        return self.repository.get_scores_by_student(student_id)