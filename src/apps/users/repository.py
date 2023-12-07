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
                name=payload.password,
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
