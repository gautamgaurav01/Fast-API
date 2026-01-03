from pydantic import BaseModel


# Define a data model for blog input using Pydantic
class Blog(BaseModel):
    title: str  # Title of the blog
    body: str  # Body/content of the blog
