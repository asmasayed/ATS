from pydantic import BaseModel, ConfigDict, EmailStr
class UserResponse(BaseModel):
    id:int
    name:str
    email:EmailStr

    #FastAPI uses Pydantic's ConfigDict to configure the model
    model_config=ConfigDict(form_attributes=True)