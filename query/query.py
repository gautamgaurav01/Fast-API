from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# Route with query parameters
@app.get("/blog")
def blog(limit: int = 10, published: bool = True, sort: Optional[str] = None):
    # Test in browser:
    # http://127.0.0.1:8000/blog?limit=5&published=false&sort=date
    # limit: number of blogs to return
    # published: True/False
    # sort: optional sorting method
    if published:
        return {"data": f"Returning {limit} unpublished blogs"}
    else:
        return {"data": f"Returning {limit} blogs"}


@app.get("/blog/unpublished")
def unpublished():
    # Test in browser:
    # http://127.0.0.1:8000/blog/unpublished
    return {"data": "unpublished blogs"}


@app.get("/blog/{id}")
def about(id: int):
    # Test in browser:
    # http://127.0.0.1:8000/blog/1
    return {"ID": id}


@app.get("/blog/{id}/comments")
def comments(id: int, limit: int = 10):
    # Test in browser:
    # http://127.0.0.1:8000/blog/1/comments
    # limit: optional limit for comments
    return {"data": ["1", "2"]}


# Pydantic model for POST request body
class Blog(BaseModel):
    title: str
    body: str
    published_at: Optional[bool]


@app.post("/blog")
def create_blog(request: Blog):
    # Test using Swagger UI:
    # http://127.0.0.1:8000/docs
    # Send JSON:
    # {
    #   "title": "My Blog",
    #   "body": "This is body",
    #   "published_at": true
    # }
    return {
        "message": "Blog created successfully",
        "title": request.title,
        "body": request.body,
        "published_at": request.published_at,
    }
