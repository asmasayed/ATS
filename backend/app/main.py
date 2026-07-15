from fastapi import FastAPI, Depends,HTTPException
from .core.config import settings
from sqlalchemy.orm import Session
from .database.database import get_db
from sqlalchemy import text

app=FastAPI(
    title=settings.PROJECT_NAME,
)

@app.get("/favicon.ico")
def get_favicon():
    return{}

@app.get("/home")
def test_home():
    return{
        "status":"healthy",
        "project":settings.PROJECT_NAME
    }

@app.get("/test-db")
def test_db(
    db:Session=Depends(get_db)
):
    try:
        result=db.execute(text("SELECT 1")).scalar()
        return{"status":"success","database_response":result}
    except Exception as e:
        raise HTTPException(
                status_code=500,
                detail=str(e)
            )
