from sqlalchemy import Column ,Integer, String ,ForeignKey
from db.database import Base


class User(Base):
    __tablename__ = "user"
    
    id = Column(Integer, primary_key=True, index=True)
    username =Column(String, unique=True)
    password = Column(String)