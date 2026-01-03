from random import randrange
from typing import Optional

from fastapi import FastAPI, HTTPException, Response, status
from fastapi.params import Body
from pydantic import BaseModel

# Initialize the FastAPI application
app = FastAPI()


# Pydantic model for validating and structuring incoming post data
class Post(BaseModel):
    title: str
    content: str
    published: bool = True  # Default value


# In-memory list simulating a database
my_posts = [
    {"title": "title of post 1", "content": "content of post 1 ", "id": 1},
    {"title": "favourite fruit", "content": "i like pizza", "id": 2},
]


# Utility function to find a post by ID and return the post object
def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p


# Utility function to return the index of a post matching the given ID
def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p["id"] == id:
            return i


# Root endpoint for basic API check
@app.get("/")
def root():
    return {"message": "Hello World"}


# GET endpoint to return all posts
@app.get("/posts")
def get_posts():
    return {"data": my_posts}


# POST endpoint to create a new post
@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    # Convert Pydantic model to dictionary and assign a random ID
    post_dict = post.dict()
    post_dict["id"] = randrange(0, 1000000)

    # Append new post to the in-memory list
    my_posts.append(post_dict)
    return {"data": post_dict}


# GET endpoint to fetch a single post by its ID
@app.get("/posts/{id}")
def get_post(id: int, response: Response):
    post = find_post(int(id))
    # Raise HTTPException if post doesn't exist
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id: {id} doesnot found",
        )
    return {"post_details": post}


# DELETE endpoint to remove a post by ID
@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    # Locate the index of the post
    index = find_index_post(id)

    # If index doesn't exist, raise an error
    if index == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id: {id} not exists",
        )

    # Remove the post from the list
    my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


# PUT endpoint to update an existing post by ID
@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    index = find_index_post(id)

    # If post is not found, raise exception
    if index == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id: {id} not exists",
        )

    # Update the post with new data but keep the same ID
    post_dict = post.dict()
    post_dict["id"] = id
    my_posts[index] = post_dict

    return {"data": post_dict}
