import typing as t
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, DeclarativeBase
from . import MYSQL_CONNECTION

class Base(DeclarativeBase):
    pass

class MySQLManager:
    def __init__(self) -> None:
        user: str = MYSQL_CONNECTION["user"]
        passwd: str = MYSQL_CONNECTION["password"]
        host: str = MYSQL_CONNECTION["host"]
        port: str = MYSQL_CONNECTION["port"]
        db: str = MYSQL_CONNECTION["db"]
        SQLALCHEMY_DATABASE_URL: t.Final[str] = f"mysql+pymysql://{user}:{passwd}@{host}:{port}/{db}?charset=utf8"

        self.engine = create_engine(
            SQLALCHEMY_DATABASE_URL, pool_size=5, pool_recycle=100, max_overflow=10
        )

    def get_session(self):
        return Session(self.engine)


if __name__ == "__main__":
    mysql_manager = MySQLManager()
