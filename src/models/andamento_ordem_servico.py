from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class AndamentoOrdemServicoIn(BaseModel):
    os_id: int
    data_hora: Optional[datetime] = None
    status_anterior_id: Optional[int] = None
    status_novo_id: Optional[int] = None
    funcionario_id: Optional[int] = None
    descricao: Optional[str] = None
    inicio_atendimento: Optional[datetime] = None
    fim_atendimento: Optional[datetime] = None

class AndamentoOrdemServicoOut(AndamentoOrdemServicoIn):
    id: int