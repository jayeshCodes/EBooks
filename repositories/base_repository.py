from sqlalchemy.orm import Session
from typing import Type, TypeVar, Generic
from sqlalchemy.exc import SQLAlchemyError

T = TypeVar('T')


class BaseRepository(Generic[T]):
    def __init__(self, db_session: Session, model: Type[T]):
        self.db_session = db_session
        self.model = model

    def get_by_id(self, id_):
        return self.db_session.query(self.model).get(id_)

    def get_all(self):
        return self.db_session.query(self.model).all()

    def add(self, entity: T):
        try:
            self.db_session.add(entity)
            self.db_session.commit()
            return entity
        except SQLAlchemyError as e:
            self.db_session.rollback()
            print(f"Error adding entity: {e}")

    def update(self, entity: T):
        try:
            self.db_session.merge(entity)
            self.db_session.commit()
        except SQLAlchemyError as e:
            self.db_session.rollback()
            print(f"Error updating entity: {e}")

    def delete(self, entity: T):
        try:
            self.db_session.delete(entity)
            self.db_session.commit()
        except SQLAlchemyError as e:
            self.db_session.rollback()
            print(f"Error deleting entity: {e}")
