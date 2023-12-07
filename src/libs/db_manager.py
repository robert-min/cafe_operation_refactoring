
import os
import json

import typing as t
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base

# TODO : conf 파일 별도 폴더로 관리
libs_path: str = os.path.abspath(os.path.join(__file__, os.path.pardir))
conf_file: str = os.path.abspath(os.path.join(libs_path, "conf.json"))
with open(conf_file, "rt") as f:
    conf = json.load(f)
MYSQL_CONNECTION = conf["mysql_connection"]

Base = declarative_base()

class MySQLManager:
    def __init__(self) -> None:
        user: str = MYSQL_CONNECTION["user"]
        passwd: str = MYSQL_CONNECTION["password"]
        host: str = MYSQL_CONNECTION["host"]
        port: str = MYSQL_CONNECTION["port"]
        db: str = MYSQL_CONNECTION["db"]
        SQLALCHEMY_DATABASE_URL: t.Final[str] = f"mysql+pymysql://{user}:{passwd}@{host}:{port}/{db}?charset=utf8"

        engine = create_engine(
            SQLALCHEMY_DATABASE_URL, pool_size=5, pool_recycle=100, max_overflow=10
        )
        self.session = Session(engine)


if __name__ == "__main__":
    mysql_manager = MySQLManager()
