from pydantic import BaseModel
from typing import Optional

class UnidadeMedidaIn(BaseModel):
    sigla: str
    descricao: Optional[str] = None

class UnidadeMedidaOut(UnidadeMedidaIn):
    id: int