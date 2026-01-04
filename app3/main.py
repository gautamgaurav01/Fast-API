from fastapi import FastAPI

from .config import settings
from .database import Base, engine
from .routers import auth, posts, users, votes

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(posts.router)
app.include_router(users.router)
app.include_router(votes.router)
app.include_router(auth.router)


@app.get("/")
def root():
    return {"message": "Hello World"}
