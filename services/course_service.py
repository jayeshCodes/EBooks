from base_service import BaseService
from repositories.course_repository import CourseRepository

class CourseService(BaseService):
    def __init__(self, course_repository: CourseRepository):
        super().__init__(course_repository)

    def get_courses_by_faculty_member(self, faculty_id):
        return self.repository.get_courses_by_faculty_member(faculty_id)
