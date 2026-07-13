#import the FastAPI class from the fastapi module
from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session

from .schemas.UserLogin import UserLogin

from .auth.security import hash_password, verify_password
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
    if db.query(User).filter(User.email==user.email).first():
        return {"LogIn Instead": "Email already registered"}
    try:
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

        return{"message":"user created"}
        
        
    except Exception as e:
        db.rollback()
        return {"error":str(e)}
        
    
@app.post("/login")
def login(
    user:UserLogin,
    db:Session=Depends(get_db)
):
    try:
        #login the user
        db_user=db.query(User).filter(User.email==user.email).first()
        if db_user is not None:
            plain_password=user.password.get_secret_value()
            hashed_password=db_user.password_hash
            authenticate=verify_password(plain_password,hashed_password)
            if not authenticate:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail={"error":"Invalid credentials"}
                )
            
            #JWT token generation can be added here for authenticated users

            return{"message":"Login successful"}
            
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail={"error":"Invalid credentials"}
            )
    except Exception as e:
        return {"error":str(e)}