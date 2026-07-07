#import the class from this module
from passlib.context import CryptContext

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