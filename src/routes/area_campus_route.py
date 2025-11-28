from fastapi import APIRouter, HTTPException
from typing import List
from models.area_campus import AreaCampusIn, AreaCampusOut
from services import area_campus_service

router = APIRouter()

@router.get("/", response_model=List[AreaCampusOut])
def listar():
    return area_campus_service.list_all()

@router.get("/{area_id}", response_model=AreaCampusOut)
def obter(area_id: int):
    a = area_campus_service.get(area_id)
    if not a:
        raise HTTPException(status_code=404, detail="Área do campus não encontrada")
    return a

@router.post("/", response_model=AreaCampusOut, status_code=201)
def criar(payload: AreaCampusIn):
    return area_campus_service.create(payload.dict())

@router.put("/{area_id}", response_model=AreaCampusOut)
def atualizar(area_id: int, payload: AreaCampusIn):
    updated = area_campus_service.update(area_id, payload.dict(exclude_unset=True))
    if not updated:
        raise HTTPException(status_code=404, detail="Área do campus não encontrada")
    return updated

@router.delete("/{area_id}", status_code=204)
def remover(area_id: int):
    ok = area_campus_service.delete(area_id)
    if not ok:
        raise HTTPException(status_code=409, detail="Registro não pode ser removido (FK ativa)")
    return None