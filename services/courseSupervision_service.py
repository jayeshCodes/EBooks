from base_service import BaseService
from repositories.courseSupervision_repository import CourseSupervisionRepository

class CourseSupervisionService(BaseService):
    def __init__(self, courseSupervisionRepository: CourseSupervisionRepository):
        super().__init__(courseSupervisionRepository)