from pydantic import BaseModel,EmailStr, SecretStr, field_validator
class UserLogin(BaseModel):
    email:EmailStr
    password:SecretStr