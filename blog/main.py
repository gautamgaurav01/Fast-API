from fastapi import FastAPI

from . import schemas

# Create FastAPI application instance
app = FastAPI()


# POST endpoint to create a new blog
@app.post("/blog")
def create(request: schemas.Blog):
    # Return the received blog data as the response
    return request
