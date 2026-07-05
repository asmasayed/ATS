from sqlalchemy import Column, DateTime, Integer, String, ForeignKey

from ..database import Base

class Application(Base):
    __tablename__="applications"
    id=Column(Integer,primary_key=True,index=True)
    user_id=Column(Integer,ForeignKey("users.id"),nullable=False)
    job_title=Column(String,nullable=False)
    company=Column(String,nullable=False)
    status=Column(String,nullable=False)
    stipend=Column(Integer,nullable=True)
    date_applied=Column(DateTime,nullable=False)
    notes=Column(String,nullable=True)
    resume_link=Column(String,nullable=True)