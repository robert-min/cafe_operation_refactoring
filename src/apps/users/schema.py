import pydantic
from datetime import datetime


class UserCreatePayload(pydantic.BaseModel):
    phone_number: str
    password: str
    name: str
    created_at: datetime = datetime.utcnow()


class UserGetPayload(pydantic.BaseModel):
    phone_number: str
