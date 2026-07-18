from pydantic import BaseModel

class StudentProfile(BaseModel):

    name: str

    rank: int

    category: str

    branch: str

    state: str

    income: int