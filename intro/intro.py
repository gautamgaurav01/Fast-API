from fastapi import FastAPI

# Create an instance of the FastAPI class
app = FastAPI()


# Route 1: Root endpoint ("/")
# Access in browser: http://127.0.0.1:8000/
# Returns a simple JSON message
@app.get("/")
def root():
    return {"data": "blog list"}


# Route 2: Unpublished blogs ("/blog/unpublished")
# Access in browser: http://127.0.0.1:8000/blog/unpublished
# Returns a JSON object with unpublished blogs
@app.get("/blog/unpublished")
def unpublished():
    return {"data": "unpublished"}


# Route 3: Blog by ID ("/blog/{id}")
# Access in browser: http://127.0.0.1:8000/blog/1
# Returns the blog ID passed in the URL
@app.get("/blog/{id}")
def about(id: int):
    return {"ID": id}


# Route 4: Comments of a blog ("/blog/{id}/comments")
# Access in browser: http://127.0.0.1:8000/blog/1/comments
# Returns a list of comments for the given blog ID
@app.get("/blog/{id}/comments")
def comments(id: int):
    # Using a list instead of a set for proper JSON response
    return {"data": ["1", "2"]}
