from pydantic import BaseModel
from typing import Optional

class EquipeManutencaoIn(BaseModel):
    nome: str
    turno: Optional[str] = None

class EquipeManutencaoOut(EquipeManutencaoIn):
    id: int