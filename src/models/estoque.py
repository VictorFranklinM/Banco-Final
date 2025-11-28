from pydantic import BaseModel
from typing import Optional

class EstoqueIn(BaseModel):
    produto_variacao_id: int
    local_estoque_id: int
    quantidade: Optional[float] = 0.0
    ponto_reposicao: Optional[float] = 0.0

class EstoqueOut(EstoqueIn):
    pass