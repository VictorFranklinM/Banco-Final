from pydantic import BaseModel
from typing import Optional

class MarcaIn(BaseModel):
    nome: Optional[str] = None

class MarcaOut(MarcaIn):
    id: int