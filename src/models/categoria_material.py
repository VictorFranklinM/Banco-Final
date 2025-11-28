from pydantic import BaseModel

class CategoriaMaterialIn(BaseModel):
    nome: str

class CategoriaMaterialOut(CategoriaMaterialIn):
    id: int