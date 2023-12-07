from sqlalchemy.orm import Session
from sqlalchemy import select
from .schema import UserCreatePayload, UserGetPayload
from .model import User

class UserRepository():
    def __init__(self, session: Session) -> None:
        self.session = session

    def create(self, payload: UserCreatePayload) -> str:
        with self.session as session:
            obj = User(
                phone_number=payload.phone_number,
                password=payload.password,
                name=payload.name,
                created_at=payload.created_at
            )
            session.add(obj)
            session.commit()
        return payload.phone_number

    def delete(self, payload: UserGetPayload) -> str:
        with self.session as session:
            sql = select(User).filter(User.phone_number == payload.phone_number)
            user = session.execute(sql).scalar_one()
            if user:
                session.delete(user)
            session.commit()
        return payload.phone_number

    def get(self, payload: UserGetPayload) -> dict:
        with self.session as session:
            sql = select(User).filter(User.phone_number == payload.phone_number)
            user = session.execute(sql).scalar_one()
            return {
                "phone_number": user.phone_number,
                "password": user.password,
                "name": user.name,
                "created_at": user.created_at
            }

    def get_all(self) -> list:
        with self.session as session:
            all_users = list()
            sql = select(User)
            for obj in session.execute(sql):
                all_users.append(obj.User.phone_number)
        return all_users
