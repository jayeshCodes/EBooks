from base_service import BaseService
from repositories.enrollment_repository import EnrollmentRepository

class EnrollmentService(BaseService):
    def __init__(self, enrollment_repository : EnrollmentRepository):
        super().__init__(enrollment_repository)

    def get_enrollments_by_course(self, course_id):
        return self.repository.get_enrollments_by_course(course_id)