from fastapi import APIRouter, HTTPException
from typing import List
from models.cor import CorIn, CorOut
from services import cor_service

router = APIRouter()

@router.get("/", response_model=List[CorOut])
def listar():
    return cor_service.list_all()

@router.get("/{cor_id}", response_model=CorOut)
def obter(cor_id: int):
    c = cor_service.get(cor_id)
    if not c:
        raise HTTPException(status_code=404, detail="Cor não encontrada")
    return c

@router.post("/", response_model=CorOut, status_code=201)
def criar(payload: CorIn):
    return cor_service.create(payload.dict())

@router.put("/{cor_id}", response_model=CorOut)
def atualizar(cor_id: int, payload: CorIn):
    updated = cor_service.update(cor_id, payload.dict(exclude_unset=True))
    if not updated:
        raise HTTPException(status_code=404, detail="Cor não encontrada")
    return updated

@router.delete("/{cor_id}", status_code=204)
def remover(cor_id: int):
    ok = cor_service.delete(cor_id)
    if not ok:
        raise HTTPException(status_code=409, detail="Registro não pode ser removido (FK ativa)")
    return None