from fastapi import APIRouter, HTTPException
from typing import List
from models.movimento_estoque import MovimentoEstoqueIn, MovimentoEstoqueOut
from services import movimento_estoque_service

router = APIRouter()

@router.get("/", response_model=List[MovimentoEstoqueOut])
def listar():
    return movimento_estoque_service.list_all()

@router.get("/{mov_id}", response_model=MovimentoEstoqueOut)
def obter(mov_id: int):
    m = movimento_estoque_service.get(mov_id)
    if not m:
        raise HTTPException(status_code=404, detail="Movimento não encontrado")
    return m

@router.post("/", response_model=MovimentoEstoqueOut, status_code=201)
def criar(payload: MovimentoEstoqueIn):
    return movimento_estoque_service.create(payload.dict())

@router.put("/{mov_id}", response_model=MovimentoEstoqueOut)
def atualizar(mov_id: int, payload: MovimentoEstoqueIn):
    updated = movimento_estoque_service.update(mov_id, payload.dict(exclude_unset=True))
    if not updated:
        raise HTTPException(status_code=404, detail="Movimento não encontrado")
    return updated

@router.delete("/{mov_id}", status_code=204)
def remover(mov_id: int):
    ok = movimento_estoque_service.delete(mov_id)
    if not ok:
        raise HTTPException(status_code=409, detail="Registro não pode ser removido (FK ativa)")
    return None