import pytest
from libs.encrypt import CipherManager

PASSWORD: str = "A123156BB3666"

@pytest.fixture
def manager():
    yield CipherManager()

@pytest.mark.asyncio
async def test_manger_to_encrypt_decrypt(manager):
    # 조건 : 유효한 비밀번호
    # 수행 : 비밀번호 암호화
    encrypt_pw = manager.encrypt_password(PASSWORD)

    # 기대하는 결과 : bytes 타입 비밀번호
    assert type(encrypt_pw) is bytes

    # 조건 : 암호화된 비밀번호
    # 수행 : 비밀번호 복호화
    decrypt_pw = manager.decrypt_password(encrypt_pw)

    # 기대하는 결과 : 원본 비밀번호와 동일
    assert type(decrypt_pw) is str
    assert decrypt_pw == PASSWORD
