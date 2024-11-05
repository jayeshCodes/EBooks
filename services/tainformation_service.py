from base_service import BaseService
from repositories.taInformation_repository import TAInformationRepository

class TAInformationService(BaseService):
    def __init__(self, ta_information_repository : TAInformationRepository):
        super().__init__(ta_information_repository)