from pydantic import BaseModel

class Ahmad_family(BaseModel):
    name: str
    age: int
    phone: int
    education: str
    currently_residing: str
    aka: str
    