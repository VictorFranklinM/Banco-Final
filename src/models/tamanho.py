from pydantic import BaseModel

class TamanhoIn(BaseModel):
    descricao: str

class TamanhoOut(TamanhoIn):
    id: int