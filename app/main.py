from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from sqlalchemy import text

from .database import SessionLocal


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def greet():
    return {"message": "This is connected to FastAPI!"}


#this is a health check fucntion
@app.get("/health/db/users")
def health_db_users(db: Session = Depends(get_db)):
    return {"count": db.execute(text("SELECT COUNT(*) FROM SpectatorSources")).scalar_one()}
