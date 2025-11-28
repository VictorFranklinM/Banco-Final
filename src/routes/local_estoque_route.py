from fastapi import APIRouter, HTTPException
from typing import List
from models.local_estoque import LocalEstoqueIn, LocalEstoqueOut
from services import local_estoque_service

router = APIRouter()

@router.get("/", response_model=List[LocalEstoqueOut])
def listar():
    return local_estoque_service.list_all()

@router.get("/{local_id}", response_model=LocalEstoqueOut)
def obter(local_id: int):
    l = local_estoque_service.get(local_id)
    if not l:
        raise HTTPException(status_code=404, detail="Local de estoque não encontrado")
    return l

@router.post("/", response_model=LocalEstoqueOut, status_code=201)
def criar(payload: LocalEstoqueIn):
    return local_estoque_service.create(payload.dict())

@router.put("/{local_id}", response_model=LocalEstoqueOut)
def atualizar(local_id: int, payload: LocalEstoqueIn):
    updated = local_estoque_service.update(local_id, payload.dict(exclude_unset=True))
    if not updated:
        raise HTTPException(status_code=404, detail="Local de estoque não encontrado")
    return updated

@router.delete("/{local_id}", status_code=204)
def remover(local_id: int):
    ok = local_estoque_service.delete(local_id)
    if not ok:
        raise HTTPException(status_code=409, detail="Registro não pode ser removido (FK ativa)")
    return None