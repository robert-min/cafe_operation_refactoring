import base64
from . import ENCRYPTION_KEY
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

class CipherManager:
    def __init__(self) -> None:
        dek = bytes(ENCRYPTION_KEY, "utf-8")
        self.Block_size = 16
        self.aes = AES.new(dek, AES.MODE_ECB)

    def encrypt_password(self, origin_pw: str) -> bytes:
        encoding_pw = pad(origin_pw.encode(), self.Block_size)
        encrypt_pw = self.aes.encrypt(encoding_pw)
        return base64.b64encode(encrypt_pw)

    def decrypt_password(self, encrypt_pw: bytes) -> str:
        decrypt_pw = self.aes.decrypt(base64.b64decode(encrypt_pw))
        origin_pw = unpad(decrypt_pw, self.Block_size).decode()
        return origin_pw
