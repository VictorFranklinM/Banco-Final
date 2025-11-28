from pydantic import BaseModel
from typing import Optional

class SetorIn(BaseModel):
    nome: str
    sigla: Optional[str] = None

class SetorOut(SetorIn):
    id: int