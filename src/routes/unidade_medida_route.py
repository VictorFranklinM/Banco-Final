from fastapi import APIRouter, HTTPException
from typing import List
from models.unidade_medida import UnidadeMedidaIn, UnidadeMedidaOut
from services import unidade_medida_service

router = APIRouter()

@router.get("/", response_model=List[UnidadeMedidaOut])
def listar():
    return unidade_medida_service.list_all()

@router.get("/{unidade_id}", response_model=UnidadeMedidaOut)
def obter(unidade_id: int):
    u = unidade_medida_service.get(unidade_id)
    if not u:
        raise HTTPException(status_code=404, detail="Unidade não encontrada")
    return u

@router.post("/", response_model=UnidadeMedidaOut, status_code=201)
def criar(payload: UnidadeMedidaIn):
    return unidade_medida_service.create(payload.dict())

@router.put("/{unidade_id}", response_model=UnidadeMedidaOut)
def atualizar(unidade_id: int, payload: UnidadeMedidaIn):
    updated = unidade_medida_service.update(unidade_id, payload.dict(exclude_unset=True))
    if not updated:
        raise HTTPException(status_code=404, detail="Unidade não encontrada")
    return updated

@router.delete("/{unidade_id}", status_code=204)
def remover(unidade_id: int):
    ok = unidade_medida_service.delete(unidade_id)
    if not ok:
        raise HTTPException(status_code=409, detail="Registro não pode ser removido (FK ativa)")
    return None