from pydantic import BaseModel

class Story(BaseModel):
    title: str
    description: str
    category: str