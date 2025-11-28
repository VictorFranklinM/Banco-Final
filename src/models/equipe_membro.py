from pydantic import BaseModel
from typing import Optional
from datetime import date

class EquipeMembroIn(BaseModel):
    equipe_id: int
    funcionario_id: int
    data_inicio: date
    data_fim: Optional[date] = None
    funcao: Optional[str] = None

class EquipeMembroOut(EquipeMembroIn):
    id: int