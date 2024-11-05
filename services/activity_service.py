from base_service import BaseService
from repositories.activity_repository import ActivityRepository

class ActivityService(BaseService):
    def __init__(self, activity_repository: ActivityRepository):
        super().__init__(activity_repository)