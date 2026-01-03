# Import core FastAPI components for building APIs
# Used for retry delay (not used here, but often helpful)
import time

# Utility to generate random numbers (not used in current code)
from random import randrange

# Used for optional type hints (not used in this file directly)
from typing import Optional

# Psycopg v3 for PostgreSQL database connection
import psycopg
from fastapi import FastAPI, HTTPException, Response, status

# Used to explicitly read request body (not required here, but commonly used)
from fastapi.params import Body

# dict_row ensures query results are returned as dictionaries instead of tuples
from psycopg.rows import dict_row

# Pydantic BaseModel for request data validation
from pydantic import BaseModel

# Initialize the FastAPI application
app = FastAPI()


# -------------------- Pydantic Schema --------------------
# Defines the structure of a post request body
class Post(BaseModel):
    title: str  # Post title (required)
    content: str  # Post content (required)
    published: bool = True  # Published status (default True)


# -------------------- Database Connection --------------------
# Keep trying to connect to PostgreSQL until successful
while True:
    try:
        conn = psycopg.connect(
            dbname="",  # Database name
            user="",  # Database username
            password="",  # Database password
            host="",  # Database host
            port=5432,  # PostgreSQL default port
            row_factory=dict_row,  # Return rows as dictionaries
        )
        cursor = conn.cursor()  # Create a cursor object
        print("Database connection was successful!")
        break
    except Exception as error:
        print("Database connection failed")
        print("Error:", error)


# -------------------- In-Memory Data (Not Used Now) --------------------
# Earlier used as a fake database before PostgreSQL integration
my_posts = [
    {"title": "title of post 1", "content": "content of post 1 ", "id": 1},
    {"title": "favourite fruit", "content": "i like pizza", "id": 2},
]


# Find a post by ID (used with in-memory data)
def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p


# Find index of a post by ID (used with in-memory data)
def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p["id"] == id:
            return i


# -------------------- API Routes --------------------


# Root endpoint to test if API is running
@app.get("/")
def root():
    return {"message": "Hello World"}


# GET all posts from PostgreSQL
@app.get("/posts")
def get_posts():
    cursor.execute("""SELECT * FROM posts""")  # Fetch all posts
    posts = cursor.fetchall()
    return {"data": posts}


# CREATE a new post
@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    cursor.execute(
        """
        INSERT INTO posts (title, content, published)
        VALUES (%s, %s, %s)
        RETURNING *
        """,
        (post.title, post.content, post.published),
    )
    new_post = cursor.fetchone()  # Fetch inserted row
    conn.commit()  # Save changes to DB
    return {"data": new_post}


# GET a single post by ID
@app.get("/posts/{id}")
def get_post(id: int):
    cursor.execute(
        """SELECT * FROM posts WHERE id = %s""",
        (str(id),),
    )
    post = cursor.fetchone()

    # If post does not exist, raise 404 error
    if post is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id: {id} does not exist",
        )
    return {"post_details": post}


# DELETE a post by ID
@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    cursor.execute(
        """DELETE FROM posts WHERE id = %s RETURNING *""",
        (str(id),),
    )
    post = cursor.fetchone()
    conn.commit()

    # If no row was deleted, post does not exist
    if post is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id: {id} does not exist",
        )

    # 204 response means success with no body
    return Response(status_code=status.HTTP_204_NO_CONTENT)


# UPDATE an existing post by ID
@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    cursor.execute(
        """
        UPDATE posts
        SET title = %s, content = %s, published = %s
        WHERE id = %s
        RETURNING *
        """,
        (post.title, post.content, post.published, str(id)),
    )
    updated_post = cursor.fetchone()
    conn.commit()

    # If no post was updated, ID does not exist
    if updated_post is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id: {id} does not exist",
        )

    return {"data": updated_post}
