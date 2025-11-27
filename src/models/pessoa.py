from pydantic import BaseModel
from typing import Optional

class PessoaIn(BaseModel):
    nome: str
    cpf: Optional[str] = None
    matricula_siape: Optional[str] = None
    email: Optional[str] = None
    telefone: Optional[str] = None
    ativo: Optional[bool] = True

class PessoaOut(PessoaIn):
    id: int