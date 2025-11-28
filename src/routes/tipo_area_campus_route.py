from fastapi import APIRouter, HTTPException
from typing import List
from models.tipo_area_campus import TipoAreaCampusIn, TipoAreaCampusOut
from services import tipo_area_campus_service

router = APIRouter()

@router.get("/", response_model=List[TipoAreaCampusOut])
def listar():
    return tipo_area_campus_service.list_all()

@router.get("/{tipo_id}", response_model=TipoAreaCampusOut)
def obter(tipo_id: int):
    t = tipo_area_campus_service.get(tipo_id)
    if not t:
        raise HTTPException(status_code=404, detail="Tipo de área não encontrado")
    return t

@router.post("/", response_model=TipoAreaCampusOut, status_code=201)
def criar(payload: TipoAreaCampusIn):
    return tipo_area_campus_service.create(payload.dict())

@router.put("/{tipo_id}", response_model=TipoAreaCampusOut)
def atualizar(tipo_id: int, payload: TipoAreaCampusIn):
    updated = tipo_area_campus_service.update(tipo_id, payload.dict(exclude_unset=True))
    if not updated:
        raise HTTPException(status_code=404, detail="Tipo de área não encontrado")
    return updated

@router.delete("/{tipo_id}", status_code=204)
def remover(tipo_id: int):
    ok = tipo_area_campus_service.delete(tipo_id)
    if not ok:
        raise HTTPException(status_code=409, detail="Registro não pode ser removido (FK ativa)")
    return None