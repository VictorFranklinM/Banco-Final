from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime

class OrdemServicoIn(BaseModel):
    numero_sequencial: Optional[str] = None
    solicitante_id: Optional[int] = None
    area_campus_id: Optional[int] = None
    tipo_os_id: Optional[int] = None
    equipe_id: Optional[int] = None
    lider_id: Optional[int] = None
    status_id: Optional[int] = None
    prioridade: Optional[int] = None
    data_abertura: Optional[datetime] = None
    data_prevista: Optional[date] = None
    descricao_problema: Optional[str] = None

class OrdemServicoOut(OrdemServicoIn):
    id: int