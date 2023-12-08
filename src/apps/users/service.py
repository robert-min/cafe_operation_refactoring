import typing as t
from .schema import UserCreatePayload, UserGetPayload
from .repository import UserRepository
from libs.db_manager import MySQLManager
from libs.exception import UserError
from libs.encrypt import CipherManager

class UserService:
    def __init__(self) -> None:
        db = MySQLManager()
        self.repo = UserRepository(db.session)
        self.encrypt_manager = CipherManager()

    def create_user(self, payload: UserCreatePayload) -> t.Optional[str]:
        if payload.phone_number in self.repo.get_all_phone_number():
            raise UserError(400, "This phone number already exists. Please log in with your existing account.")

        user_info = payload.dict()
        user_info["password"] = self.encrypt_manager.encrypt_password(user_info["password"])
        return self.repo.create(user_info)

    def delete_user(self, payload: UserGetPayload) -> t.Optional[str]:
        user_id = payload.phone_number
        return self.repo.delete(user_id)

    def get_user(self, payload: UserGetPayload) -> t.Optional[dict]:
        user_id = payload.phone_number
        user_info = self.repo.get(user_id)
        if not user_info:
            raise UserError(404, "Invalid phone number. Please check your phone number.")

        user_info["password"] = self.encrypt_manager.decrypt_password(user_info["password"])
        return user_info
