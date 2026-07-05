from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

#Load the database URL
load_dotenv()
DATABASE_URL=os.getenv("DATABASE_URL")

#Create the db engine object, create_engine returns a new instance of Engine class
engine=create_engine(DATABASE_URL)

#Create the session local class
SessionLocal=sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False
)

#Call dec_base() is a factory function that constructs a base class, Base
Base=declarative_base()
