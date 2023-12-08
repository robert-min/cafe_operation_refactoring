import pytest
from libs.db_manager import MySQLManager
from apps.users.repository import UserRepository
from apps.users.schema import UserCreatePayload, UserGetPayload


PHONE_NUMBER: str = "010-0000-0000"
PASSWORD: str = "1234"
NAME: str = "kim"

# TODO : 비동기 처리 학습 후 _loop = asyncio.get_event_loop() 문제 해결!!
@pytest.fixture
def repository():
    session = MySQLManager().get_session()
    yield UserRepository(session)

@pytest.mark.order(1)
@pytest.mark.asyncio
async def test_user_repository_can_create_user_with_valid(repository):
    # 주어진 조건 : 유효한 회원가입 정보
    payload = UserCreatePayload(
        phone_number=PHONE_NUMBER,
        password=PASSWORD,
        name=NAME)
    user_info = payload.dict()
    # 수행 : 회원가입
    result = repository.create(user_info)

    # 기대하는 결과 : phone_number 반환
    assert result == PHONE_NUMBER

@pytest.mark.order(2)
@pytest.mark.asyncio
async def test_user_repository_can_get_user_with_valid(repository):
    # 주어진 조건 : 유효한 휴대폰 번호
    payload = UserGetPayload(phone_number=PHONE_NUMBER)
    user_id = payload.phone_number

    # 수행 : 유저 정보 조회
    result = repository.get(user_id)

    # 기대하는 결과 : 유저 정보 반환
    assert result["phone_number"] == PHONE_NUMBER
    assert result["password"] == PASSWORD
    assert result["name"] == NAME
    
@pytest.mark.order(3)
@pytest.mark.asyncio
async def test_user_repository_can_get_all_user(repository):
    # 수행 : 유저 전체 정보 조회
    result = repository.get_all_phone_number()

    # 기대하는 결과 : 유저 전체 정보 수 1개 이상
    assert len(result) >= 1

@pytest.mark.order(4)
@pytest.mark.asyncio
async def test_user_repository_can_delete_user_with_valid_payload(repository):
    # 주어진 조건 : 유효한 휴대폰 번호
    payload = UserGetPayload(phone_number=PHONE_NUMBER)
    user_id = payload.phone_number

    # 수행 : 유저 삭제
    result = repository.delete(user_id)

    # 기대하는 결과 : phone_number 반환
    assert result == PHONE_NUMBER
