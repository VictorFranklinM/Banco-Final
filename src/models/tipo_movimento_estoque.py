from pydantic import BaseModel
from typing import Optional

class TipoMovimentoEstoqueIn(BaseModel):
    descricao: Optional[str] = None
    sinal: Optional[str] = None

class TipoMovimentoEstoqueOut(TipoMovimentoEstoqueIn):
    id: int