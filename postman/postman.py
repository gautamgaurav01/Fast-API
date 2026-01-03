from fastapi import FastAPI
from pydantic import BaseModel

# Initialize the FastAPI application
app = FastAPI()


# Pydantic model for request validation
class Post(BaseModel):
    title: str
    content: str
    published: bool = True  # Default value


# Root route
@app.get("/")
def root():
    return {"message": "Hello World"}


# GET route to fetch posts
@app.get("/posts")
def get_posts():
    return {"data": "This is a posts"}


# POST route to create a new post
@app.post("/createposts")
def create_posts(post: Post):
    # Automatically validates and converts incoming JSON into Post model
    print(post)
    print(post.dict())
    return {"data": "post"}
