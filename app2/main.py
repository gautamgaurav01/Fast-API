from typing import List, Optional

from fastapi import Depends, FastAPI, HTTPException, Response, status
from sqlalchemy.orm import Session

from . import create_table, schemas, utils
from .database import Base, engine, get_db
from .routers import posts, users

Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(posts.router)
app.include_router(users.router)


@app.get("/")
def root():
    return {"message": "Hello World"}
