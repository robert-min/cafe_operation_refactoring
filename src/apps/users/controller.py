from fastapi import APIRouter, Depends
from .schema import UserCreatePayload
from .service import UserService
from libs.db_manager import MySQLManager
from sqlalchemy.orm import Session

auth = APIRouter(prefix="/auth")

@auth.post("/signup")
async def signup(
    payload: UserCreatePayload,
    session: Session = Depends(MySQLManager().get_session)
):
    return {
        "meta": {
            "code": 200,
            "message": "ok"
        },
        "data": UserService(session).create_user(payload)
    }
