from fastapi import APIRouter, Depends
from .schema import UserCreatePayload
from .service import UserService
from libs.db_manager import MySQLManager
from libs.util import make_response
from sqlalchemy.orm import Session

auth = APIRouter(prefix="/auth")
@auth.post("/signup")
async def signup(
    payload: UserCreatePayload,
    session: Session = Depends(MySQLManager().get_session)
):
    resp = UserService(session).create_user(payload)
    return make_response(str(resp))
