from pydantic import BaseModel
from typing import Optional

class TipoAreaCampusIn(BaseModel):
    descricao: Optional[str] = None

class TipoAreaCampusOut(TipoAreaCampusIn):
    id: int