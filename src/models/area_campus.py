from pydantic import BaseModel
from typing import Optional

class AreaCampusIn(BaseModel):
    tipo_area_id: int
    descricao: str
    bloco: Optional[str] = None

class AreaCampusOut(AreaCampusIn):
    id: int