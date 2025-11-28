from pydantic import BaseModel
from typing import Optional

class LocalEstoqueIn(BaseModel):
    descricao: Optional[str] = None
    responsavel_id: Optional[int] = None

class LocalEstoqueOut(LocalEstoqueIn):
    id: int