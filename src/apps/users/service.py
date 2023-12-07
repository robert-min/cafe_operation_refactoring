from .schema import UserCreatePayload, UserGetPayload
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

    def delete_user(self, payload: UserGetPayload):
        return self.repo.delete(payload)

    def get_user(self, payload: UserGetPayload):
        user = self.repo.get(payload)
        if not user:
            raise UserError(404, "Invalid phone number. Please check your phone number.")
        
        # TODO : 비밀번호 복호화
        return user
