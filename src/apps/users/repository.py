from sqlalchemy.orm import Session
from .schema import UserSignUpPayload
from .model import User

class UserRepository():
    def __init__(self, session: Session) -> None:
        self.session = session

    def create(self, payload: UserSignUpPayload) -> str:
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
