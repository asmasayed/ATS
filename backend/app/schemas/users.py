from pydantic import BaseModel, EmailStr, SecretStr, field_validator

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: SecretStr

    @field_validator('password')
    @classmethod
    def validate_password(cls, value:SecretStr)->SecretStr:
        password=value.get_secret_value()
        if(len(password)<4):
            raise ValueError("Password must be at least 4 characters long")
        if not any(char.isdigit() for char in password):
            raise ValueError("Password must contain at least one digit")
        if not any(char.isupper() for char in password):
            raise ValueError("Password must contain at least one uppercase letter")
        return value