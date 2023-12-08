import typing as t
from sqlalchemy.orm import Session
from sqlalchemy import select
from .model import User
from libs.exception import UserRepositoryError

# TODO : STATUS CODE 별도 파일로 관리
USER_REPOSITORY_CODE: int = 500

class UserRepository():
    def __init__(self, session: Session) -> None:
        self.session = session

    def create(self, user_info: dict) -> t.Optional[str]:
        try:
            with self.session as session:
                obj = User(
                    phone_number=user_info["phone_number"],
                    password=user_info["password"],
                    name=user_info["name"],
                    created_at=user_info["created_at"]
                )
                session.add(obj)
                session.commit()
            return user_info["phone_number"]
        except Exception as e:
            UserRepositoryError(USER_REPOSITORY_CODE, "Failed to create user", e)

    def delete(self, user_id: str) -> t.Optional[str]:
        try:
            with self.session as session:
                sql = select(User).filter(User.phone_number == user_id)
                obj = session.execute(sql).scalar_one()
                if obj:
                    session.delete(obj)
                session.commit()
            return user_id
        except Exception as e:
            UserRepositoryError(USER_REPOSITORY_CODE, "Failed to delete user", e)

    def get(self, user_id: str) -> t.Optional[dict]:
        try:
            with self.session as session:
                sql = select(User).filter(User.phone_number == user_id)
                obj = session.execute(sql).scalar_one()
                return {
                    "phone_number": obj.phone_number,
                    "password": obj.password,
                    "name": obj.name,
                    "created_at": obj.created_at
                }
        except Exception as e:
            UserRepositoryError(USER_REPOSITORY_CODE, "Failed to get user", e)

    def get_all_phone_number(self) -> list:
        try:
            with self.session as session:
                all_users = list()
                sql = select(User)
                for obj in session.execute(sql):
                    all_users.append(obj.User.phone_number)
            return all_users
        except Exception as e:
            UserRepositoryError(USER_REPOSITORY_CODE, "Failed to get all user", e)
