#import the FastAPI class from the fastapi module
from fastapi import FastAPI

#This creates your backend and assigns it to the object app
app=FastAPI()

#Whenever someone sends a GET request to "/" run this function
@app.get("/")

#this function runs whenever someone visits http://localhost:8000/
def root():
    #returns a dictionary with a key of "message" and a value of "Hello World!". FastAPI will automatically convert this dictionary to JSON and send it to the client.
    return {"message": "Hello World!"}
