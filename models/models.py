from datetime import datetime
from sqlalchemy import Column ,Integer, String ,ForeignKey, DateTime
from db.database import Base


class User(Base):
    __tablename__ = "user"
    
    id = Column(Integer, primary_key=True, index=True)
    username =Column(String, unique=True)
    password = Column(String)
    role = Column(String, default="user")

class Announcement(Base):
    __tablename__ = "announcement"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    author = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow())