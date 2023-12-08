import pytest
from fastapi import status

PHONE_NUMBER: str = "010-0000-0000"
PASSWORD: str = "1234"
NAME: str = "kim"


@pytest.mark.order(1)
@pytest.mark.asyncio
async def test_user_controller_can_signup_with_valid(client):
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

@pytest.mark.order(2)
@pytest.mark.asyncio
async def test_user_controller_cannot_signup_with_existence(client):
    # 조건 : 이미 생성된 phone_number로 계정 생성 요청
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

    # 기대하는 결과 : 400, phone_number 반환
    assert res.status_code == 400
    data = res.json()
    assert data["meta"]["code"] == 400
    assert data["meta"]["message"] == "This phone number already exists. Please log in with your existing account."
