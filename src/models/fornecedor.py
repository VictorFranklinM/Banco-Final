from pydantic import BaseModel
from typing import Optional

class FornecedorIn(BaseModel):
    nome: Optional[str] = None
    cnpj: Optional[str] = None

class FornecedorOut(FornecedorIn):
    id: int