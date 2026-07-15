from ..database.base import Base
from sqlalchemy.orm import mapped_column, Mapped 
from sqlalchemy import String, Enum, DateTime, func
import enum
from datetime import datetime

class UserRole(str,enum.Enum):
    ADMIN="admin"
    USER="user"

class User(Base):
    __tablename__="users"
    id: Mapped[int]= mapped_column(primary_key=True,index=True) 

    name:Mapped[str]=mapped_column(String(255),nullable=False)
    
    email:Mapped[str]= mapped_column(String(255), unique=True, index=True, nullable=False)

    hashed_password:Mapped[str]=mapped_column(String(255),nullable=False)

    role:Mapped[UserRole]=mapped_column(Enum(UserRole),default=UserRole.USER,nullable=False)

    created_at: Mapped[datetime]=mapped_column(
        DateTime(timezone=True),server_default=func.now()
    )

    updated_at:Mapped[datetime]=mapped_column(
        DateTime(timezone=True),server_default=func.now(), onupdate=func.now()
    )