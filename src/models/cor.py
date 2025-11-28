from pydantic import BaseModel

class CorIn(BaseModel):
    nome: str

class CorOut(CorIn):
    id: int