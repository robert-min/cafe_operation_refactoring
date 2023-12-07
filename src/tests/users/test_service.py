import pytest
from apps.users.schema import UserCreatePayload, UserGetPayload
from apps.users.service import UserService
from libs.exception import UserError

PHONE_NUMBER: str = "010-0000-0000"
PASSWORD: str = "1234"
NAME: str = "kim"

@pytest.fixture
def service():
    yield UserService()

@pytest.mark.order(1)
@pytest.mark.asyncio
async def test_user_service_can_create_user_with_valid(service):
    # 주어진 조건 : 유효한 회원가입 정보
    payload = UserCreatePayload(
        phone_number=PHONE_NUMBER,
        password=PASSWORD,
        name=NAME)

    # 수행 : 회원가입
    result = service.create_user(payload)

    # 기대하는 결과 : phone_number 반환
    assert result == PHONE_NUMBER

@pytest.mark.order(2)
@pytest.mark.asyncio
async def test_user_service_cannot_create_user_with_existence(service):
    # 주어진 조건 : 이미 생성된 회원 정보로 다시 회원가입 요청
    payload = UserCreatePayload(
        phone_number=PHONE_NUMBER,
        password=PASSWORD,
        name=NAME)

    # 수행 : 회원가입
    with pytest.raises(UserError) as error:
        service.create_user(payload)

    # 기대하는 결과 : error code, message 반환
    assert error.value.code == 400
    assert error.value.message == "This phone number already exists. Please log in with your existing account."

@pytest.mark.order(3)
@pytest.mark.asyncio
async def test_user_service_can_get_user_with_valid(service):
    # 주어진 조건 : 유효한 휴대폰 번호
    payload = UserGetPayload(phone_number=PHONE_NUMBER)

    # 수행 : 유저 정보 반환
    result = service.get_user(payload)

    # 기대하는 결과 : 유저정보 반환
    assert result["phone_number"] == PHONE_NUMBER
    assert result["password"] == PASSWORD
    assert result["name"] == NAME

@pytest.mark.order(4)
@pytest.mark.asyncio
async def test_user_service_cannot_get_user_with_invalid(service):
    # 주어진 조건 : 유효한 휴대폰 번호
    payload = UserGetPayload(phone_number="010")

    # 수행 : 유저 정보 반환
    with pytest.raises(UserError) as error:
        service.get_user(payload)

    # 기대하는 결과 : error code, message 반환
    assert error.value.code == 404
    assert error.value.message == "Invalid phone number. Please check your phone number."

@pytest.mark.order(5)
@pytest.mark.asyncio
async def test_user_service_can_delete_user_with_valid(service):
    # 주어진 조건 : 유효한 휴대폰 번호
    payload = UserGetPayload(phone_number=PHONE_NUMBER)

    # 수행 : 유저 삭제
    result = service.delete_user(payload)

    # 기대하는 결과 : phone_number 반환
    assert result == PHONE_NUMBER
