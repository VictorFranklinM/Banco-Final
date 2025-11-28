from fastapi import APIRouter, HTTPException
from typing import List
from models.tipo_movimento_estoque import TipoMovimentoEstoqueIn, TipoMovimentoEstoqueOut
from services import tipo_movimento_estoque_service

router = APIRouter()

@router.get("/", response_model=List[TipoMovimentoEstoqueOut])
def listar():
    return tipo_movimento_estoque_service.list_all()

@router.get("/{tipo_id}", response_model=TipoMovimentoEstoqueOut)
def obter(tipo_id: int):
    t = tipo_movimento_estoque_service.get(tipo_id)
    if not t:
        raise HTTPException(status_code=404, detail="Tipo de movimento não encontrado")
    return t

@router.post("/", response_model=TipoMovimentoEstoqueOut, status_code=201)
def criar(payload: TipoMovimentoEstoqueIn):
    return tipo_movimento_estoque_service.create(payload.dict())

@router.put("/{tipo_id}", response_model=TipoMovimentoEstoqueOut)
def atualizar(tipo_id: int, payload: TipoMovimentoEstoqueIn):
    updated = tipo_movimento_estoque_service.update(tipo_id, payload.dict(exclude_unset=True))
    if not updated:
        raise HTTPException(status_code=404, detail="Tipo de movimento não encontrado")
    return updated

@router.delete("/{tipo_id}", status_code=204)
def remover(tipo_id: int):
    ok = tipo_movimento_estoque_service.delete(tipo_id)
    if not ok:
        raise HTTPException(status_code=409, detail="Registro não pode ser removido (FK ativa)")
    return None