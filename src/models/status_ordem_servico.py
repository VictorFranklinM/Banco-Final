from pydantic import BaseModel
from typing import Optional

class StatusOrdemServicoIn(BaseModel):
    descricao: Optional[str] = None

class StatusOrdemServicoOut(StatusOrdemServicoIn):
    id: int