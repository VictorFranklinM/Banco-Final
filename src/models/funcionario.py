from pydantic import BaseModel
from typing import Optional
from datetime import date

class FuncionarioIn(BaseModel):
    pessoa_id: int
    tipo_funcionario_id: Optional[int] = None
    setor_id: Optional[int] = None
    data_admissao: Optional[date] = None
    data_demissao: Optional[date] = None

class FuncionarioOut(FuncionarioIn):
    id: int