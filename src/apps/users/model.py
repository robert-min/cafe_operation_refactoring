from sqlalchemy import Column, Integer, VARCHAR
from libs.db_manager import Base


class User(Base):
    __tablename__ = "user_info"
    # issue : https://docs.sqlalchemy.org/en/20/orm/declarative_tables.html#declarative-table-configuration
    __table_args__ = {'extend_existing': True} 

    seq: Column = Column(Integer, primary_key=True, index=True)
    phone_number: Column = Column(VARCHAR, unique=True)
    password: Column = Column(VARCHAR, unique=True)
    name: Column = Column(VARCHAR, unique=True)
    created_at: Column = Column(VARCHAR, unique=True)

    def __repr__(self):
        return f"User(id={self.seq}, phone_number={self.phone_number}, created_at={self.created_at})"

    def __str__(self):
        return self.__repr__()
