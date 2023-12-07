from .schema import UserCreatePayload
from .repository import UserRepository
from libs.db_manager import MySQLManager
from libs.exception import UserError

class UserService:
    def __init__(self) -> None:
        db = MySQLManager()
        self.repo = UserRepository(db.session)

    def create_user(self, payload: UserCreatePayload):
        if payload.phone_number in self.repo.get_all():
            raise UserError(400, "This phone number already exists. Please log in with your existing account.")

        # TODO : 비밀번호 암호화
        return self.repo.create(payload)
