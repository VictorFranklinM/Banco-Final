from pydantic import BaseModel
from typing import Optional

class ProdutoIn(BaseModel):
    descricao: str
    categoria_id: Optional[int] = None
    unidade_medida_id: Optional[int] = None
    marca_id: Optional[int] = None

class ProdutoOut(ProdutoIn):
    id: int