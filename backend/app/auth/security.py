#import the class from this module
from datetime import datetime,timezone,timedelta
from jose import jwt
from passlib.context import CryptContext


from fastapi import HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError 
import os

from sqlalchemy.orm import Session
from ..database import get_db
from ..models.user import User
from fastapi.params import Depends


SUPER_SECRET_KEY=os.getenv("SUPER_SECRET_KEY")
ALGORITHM=os.getenv("ALGORITHM")

#Use this reusable CryptContext to hash and verify passwords. 
pwd_context=CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

def hash_password(password: str)->str:
    #Ask the configured CryptContext to hash this password
    return pwd_context.hash(password)

def verify_password(plain_password:str, hashed_password:str)->bool:
    return pwd_context.verify(plain_password,hashed_password)

def create_access_token(data:dict):
    to_encode=data.copy()
    expire=datetime.now(timezone.utc)+timedelta(minutes=30)
    to_encode.update({"exp":expire})
    return jwt.encode(to_encode, SUPER_SECRET_KEY, algorithm=ALGORITHM)


#Create a dependency using OAuth2PasswordBearer to extract the token from headers
oauth2_scheme=OAuth2PasswordBearer(
    tokenUrl="/login",
)

def get_current_user(
    token:str=Depends(oauth2_scheme),
    db:Session=Depends(get_db)
):
    try:
        #return a python dictionary
        payload=jwt.decode(token, SUPER_SECRET_KEY, algorithms=[ALGORITHM])
        
        user_id=payload.get("sub")
        if user_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token"
            )
        db_user=db.query(User).filter(User.id==user_id).first()
        if db_user is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="User not found"
            )
        return db_user
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials"
        )