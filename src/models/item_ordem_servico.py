from pydantic import BaseModel
from typing import Optional

class ItemOrdemServicoIn(BaseModel):
    os_id: int
    produto_variacao_id: int
    quantidade_prevista: Optional[float] = None
    quantidade_usada: Optional[float] = None

class ItemOrdemServicoOut(ItemOrdemServicoIn):
    id: int