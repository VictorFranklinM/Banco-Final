from pydantic import BaseModel
from typing import Optional

class ProdutoVariacaoIn(BaseModel):
    produto_id: int
    cor_id: Optional[int] = None
    tamanho_id: Optional[int] = None
    codigo_barras: Optional[str] = None
    codigo_interno: Optional[str] = None

class ProdutoVariacaoOut(ProdutoVariacaoIn):
    id: int