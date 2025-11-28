from pydantic import BaseModel
from typing import Optional

class TipoOrdemServicoIn(BaseModel):
    descricao: Optional[str] = None

class TipoOrdemServicoOut(TipoOrdemServicoIn):
    id: int