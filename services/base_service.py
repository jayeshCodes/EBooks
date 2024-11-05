class BaseService:
    def __init__(self, repository):
        self.repository = repository

    def get_all(self):
        return self.repository.get_all()

    def get_by_id(self, id_):
        return self.repository.get_by_id(id_)

    def create(self, data):
        return self.repository.create(data)

    def update(self, id_, data):
        return self.repository.update(id_, data)

    def delete(self, id_):
        return self.repository.delete(id_)
    