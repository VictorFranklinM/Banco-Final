from fastapi import APIRouter, HTTPException
from typing import List
from models.tamanho import TamanhoIn, TamanhoOut
from services import tamanho_service

router = APIRouter()

@router.get("/", response_model=List[TamanhoOut])
def listar():
    return tamanho_service.list_all()

@router.get("/{tamanho_id}", response_model=TamanhoOut)
def obter(tamanho_id: int):
    t = tamanho_service.get(tamanho_id)
    if not t:
        raise HTTPException(status_code=404, detail="Tamanho não encontrado")
    return t

@router.post("/", response_model=TamanhoOut, status_code=201)
def criar(payload: TamanhoIn):
    return tamanho_service.create(payload.dict())

@router.put("/{tamanho_id}", response_model=TamanhoOut)
def atualizar(tamanho_id: int, payload: TamanhoIn):
    updated = tamanho_service.update(tamanho_id, payload.dict(exclude_unset=True))
    if not updated:
        raise HTTPException(status_code=404, detail="Tamanho não encontrado")
    return updated

@router.delete("/{tamanho_id}", status_code=204)
def remover(tamanho_id: int):
    ok = tamanho_service.delete(tamanho_id)
    if not ok:
        raise HTTPException(status_code=409, detail="Registro não pode ser removido (FK ativa)")
    return None