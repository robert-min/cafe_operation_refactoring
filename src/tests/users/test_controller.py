import pytest
from fastapi import status
from libs.db_manager import MySQLManager

PHONE_NUMBER: str = "010-0000-0000"
PASSWORD: str = "1234"
NAME: str = "kim"

@pytest.fixture
def session():
    session = MySQLManager().get_session()
    yield session

@pytest.mark.order(1)
@pytest.mark.asyncio
async def test_user_controller_signup_with_valid(client, session):
    # 조건 : 유효한 parameter
    params = {
        "phone_number": PHONE_NUMBER,
        "password": PASSWORD,
        "name": NAME
    }

    # 수행 : 회원가입 API 요청
    res = client.post(
        "/auth/signup",
        json=params
    )

    # 기대하는 결과 : 200, phone_number 반환
    assert res.status_code == status.HTTP_200_OK
    data = res.json()
    assert data["data"] == PHONE_NUMBER

