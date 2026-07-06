#import the FastAPI class from the fastapi module
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from .auth.security import hash_password
from .schemas.users import UserCreate
from .database import engine, Base
from .models.user import User
from .models.application import Application
from .models.resume import Resume
from .database import  get_db

#This creates your backend and assigns it to the object app
app=FastAPI()

#Whenever someone sends a GET request to "/" run this function
@app.get("/")

#this function runs whenever someone visits http://localhost:8000/
def root():
    #returns a dictionary with a key of "message" and a value of "Hello World!". FastAPI will automatically convert this dictionary to JSON and send it to the client.
    return {"message": "Hello World!"}

#Gather all models and create the tables
#(only use this in development)
#Base.metadata.create_all(bind=engine)

#Create endpoint for signup
@app.post("/signup")
def signup(
    user: UserCreate,

    # Ask FastAPI to provide a database Session using get_db()
    db: Session=Depends(get_db)
    ):
    hashed_password=hash_password(user.password.get_secret_value())


    #Create a new user object
    db_user=User(
        name=user.name,
        email=user.email,
        password_hash=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {"message": "User created"} 