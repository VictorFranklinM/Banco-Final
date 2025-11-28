from fastapi import APIRouter, HTTPException
from typing import List
from models.produto_variacao import ProdutoVariacaoIn, ProdutoVariacaoOut
from services import produto_variacao_service

router = APIRouter()

@router.get("/", response_model=List[ProdutoVariacaoOut])
def listar():
    return produto_variacao_service.list_all()

@router.get("/{var_id}", response_model=ProdutoVariacaoOut)
def obter(var_id: int):
    v = produto_variacao_service.get(var_id)
    if not v:
        raise HTTPException(status_code=404, detail="Variação não encontrada")
    return v

@router.post("/", response_model=ProdutoVariacaoOut, status_code=201)
def criar(payload: ProdutoVariacaoIn):
    return produto_variacao_service.create(payload.dict())

@router.put("/{var_id}", response_model=ProdutoVariacaoOut)
def atualizar(var_id: int, payload: ProdutoVariacaoIn):
    updated = produto_variacao_service.update(var_id, payload.dict(exclude_unset=True))
    if not updated:
        raise HTTPException(status_code=404, detail="Variação não encontrada")
    return updated

@router.delete("/{var_id}", status_code=204)
def remover(var_id: int):
    ok = produto_variacao_service.delete(var_id)
    if not ok:
        raise HTTPException(status_code=409, detail="Registro não pode ser removido (FK ativa)")
    return None