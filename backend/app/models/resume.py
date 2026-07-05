from sqlalchemy import Column, DateTime, Integer, String, ForeignKey

from ..database import Base

class Resume(Base):
    __tablename__="resumes"
    id=Column(Integer,primary_key=True,index=True)
    user_id=Column(Integer,ForeignKey("users.id"),nullable=False)
    title=Column(String,nullable=False)
    file_url=Column(String,nullable=False)
    uploaded_at=Column(DateTime,nullable=False)