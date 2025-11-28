from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class MovimentoEstoqueIn(BaseModel):
    produto_variacao_id: int
    local_estoque_id: int
    tipo_movimento_id: int
    quantidade: float
    data_hora: Optional[datetime] = None
    funcionario_id: Optional[int] = None
    ordem_servico_id: Optional[int] = None
    observacao: Optional[str] = None

class MovimentoEstoqueOut(MovimentoEstoqueIn):
    id: int