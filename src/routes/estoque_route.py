from fastapi import APIRouter, HTTPException
from typing import List
from models.estoque import EstoqueIn, EstoqueOut
from services import estoque_service

router = APIRouter()

@router.get("/", response_model=List[EstoqueOut])
def listar():
    return estoque_service.list_estoque()

@router.get("/{produto_variacao_id}/{local_estoque_id}", response_model=EstoqueOut)
def obter(produto_variacao_id: int, local_estoque_id: int):
    e = estoque_service.get_estoque(produto_variacao_id, local_estoque_id)
    if not e:
        raise HTTPException(status_code=404, detail="Registro de estoque não encontrado")
    return e

@router.post("/", response_model=EstoqueOut, status_code=201)
def criar(payload: EstoqueIn):
    return estoque_service.create_estoque(payload.dict())

@router.put("/{produto_variacao_id}/{local_estoque_id}", response_model=EstoqueOut)
def atualizar(produto_variacao_id: int, local_estoque_id: int, payload: EstoqueIn):
    updated = estoque_service.update_estoque(produto_variacao_id, local_estoque_id, payload.dict(exclude_unset=True))
    if not updated:
        raise HTTPException(status_code=404, detail="Registro de estoque não encontrado")
    return updated

@router.delete("/{produto_variacao_id}/{local_estoque_id}", status_code=204)
def remover(produto_variacao_id: int, local_estoque_id: int):
    ok = estoque_service.delete_estoque(produto_variacao_id, local_estoque_id)
    if not ok:
        raise HTTPException(status_code=409, detail="Registro não pode ser removido (FK ativa)")
    return None
