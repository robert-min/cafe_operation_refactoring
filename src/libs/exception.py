class CustomHttpException(Exception):
    def __init__(self, code: int, message: str) -> None:
        self.code = code
        self.message = message
        self.error = None

class UserError(CustomHttpException):
    def __init__(self, code: int, message: str) -> None:
        super().__init__(code, message)

class UserRepositoryError(CustomHttpException):
    def __init__(self, code: int, message: str, error: Exception) -> None:
        super().__init__(code, message)
        self.error = error

class ServiceError(CustomHttpException):
    # logging 추가
    def __init__(self, code: int, message: str, error: Exception) -> None:
        super().__init__(code, message)
        self.error = error
