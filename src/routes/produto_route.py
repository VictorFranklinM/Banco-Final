from fastapi import APIRouter, HTTPException
from typing import List
from models.produto import ProdutoIn, ProdutoOut
from services import produto_service

router = APIRouter()

@router.get("/", response_model=List[ProdutoOut])
def listar():
    return produto_service.list_all()

@router.get("/{produto_id}", response_model=ProdutoOut)
def obter(produto_id: int):
    p = produto_service.get(produto_id)
    if not p:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return p

@router.post("/", response_model=ProdutoOut, status_code=201)
def criar(payload: ProdutoIn):
    return produto_service.create(payload.dict())

@router.put("/{produto_id}", response_model=ProdutoOut)
def atualizar(produto_id: int, payload: ProdutoIn):
    updated = produto_service.update(produto_id, payload.dict(exclude_unset=True))
    if not updated:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return updated

@router.delete("/{produto_id}", status_code=204)
def remover(produto_id: int):
    ok = produto_service.delete(produto_id)
    if not ok:
        raise HTTPException(status_code=409, detail="Registro não pode ser removido (FK ativa)")
    return None