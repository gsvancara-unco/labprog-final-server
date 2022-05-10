from pydantic import BaseModel

class Image(BaseModel):
    url: str
    height: int
    width: int

class Story(BaseModel):
    title: str
    abstract: str
    url: str
    published_date: str
