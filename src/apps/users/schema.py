import pydantic
from datetime import datetime


class UserSignUpPayload(pydantic.BaseModel):
    phone_number: str
    password: str
    name: str
    created_at: datetime = datetime.utcnow()
