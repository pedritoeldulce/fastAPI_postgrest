from pydantic import BaseModel


class Course(BaseModel):
    # id: int
    name: str
    title: str
    description: str
    url: str
    module: int
    chapter: int
    category: str
    status: str
