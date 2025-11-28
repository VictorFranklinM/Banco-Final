from fastapi import APIRouter, HTTPException
from typing import List
from models.marca import MarcaIn, MarcaOut
from services import marca_service

router = APIRouter()

@router.get("/", response_model=List[MarcaOut])
def listar():
    return marca_service.list_all()

@router.get("/{marca_id}", response_model=MarcaOut)
def obter(marca_id: int):
    m = marca_service.get(marca_id)
    if not m:
        raise HTTPException(status_code=404, detail="Marca não encontrada")
    return m

@router.post("/", response_model=MarcaOut, status_code=201)
def criar(payload: MarcaIn):
    return marca_service.create(payload.dict())

@router.put("/{marca_id}", response_model=MarcaOut)
def atualizar(marca_id: int, payload: MarcaIn):
    updated = marca_service.update(marca_id, payload.dict(exclude_unset=True))
    if not updated:
        raise HTTPException(status_code=404, detail="Marca não encontrada")
    return updated

@router.delete("/{marca_id}", status_code=204)
def remover(marca_id: int):
    ok = marca_service.delete(marca_id)
    if not ok:
        raise HTTPException(status_code=409, detail="Registro não pode ser removido (FK ativa)")
    return None