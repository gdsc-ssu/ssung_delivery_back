from sqlalchemy import Column, Integer, String, Boolean, DateTime, MetaData
from sqlalchemy.sql.expression import func
from database import *


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String(30), nullable=False, unique=True)
    password = Column(String(200), nullable=False)
    address = Column(String(50), nullable=False)
    is_user = Column(Boolean, nullable=False)
    created_at = Column(DateTime, default=func.now())

# if __name__ == '__main__':
    # Base.metadata.create_all(engine)