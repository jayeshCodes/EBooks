from base_service import BaseService
from repositories.person_repository import PersonRepository


class PersonService(BaseService):
    def __init__(self, person_repository: PersonRepository):
        super().__init__(person_repository)

    def get_person_by_email(self, email):
        return self.repository.get_person_by_email(email)
