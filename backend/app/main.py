#import the FastAPI class from the fastapi module
from fastapi import FastAPI
from .database import engine, Base
from .models.user import User
from .models.application import Application
from .models.resume import Resume

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