import pytest
from libs.db_manager import MySQLManager
from apps.users.repository import UserRepository
from apps.users.schema import UserSignUpPayload


PHONE_NUMBER: str = "010-0000-0000"
PASSWORD: str = "1234"
NAME: str = "kim"

@pytest.fixture
def repository():
    db = MySQLManager()
    yield UserRepository(db.session)

@pytest.mark.asyncio
def test_user_repository_can_create_user_with_valid_payload(repository):
    # 주어진 조건
    #   - 유효한 회원가입 정보
    payload = UserSignUpPayload(
        phone_number=PHONE_NUMBER,
        password=PASSWORD,
        name=NAME)

    # 수행
    #   - 회원가입
    result = repository.create(payload)

    # 기대하는 결과
    #   - phone_number 반환
    assert result == "010-0000-0000"
