from pydantic import BaseModel

class TipoFuncionarioIn(BaseModel):
    descricao: str

class TipoFuncionarioOut(TipoFuncionarioIn):
    id: int