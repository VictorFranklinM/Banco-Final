from fastapi import APIRouter, HTTPException
from typing import List
from models.fornecedor import FornecedorIn, FornecedorOut
from services import fornecedor_service

router = APIRouter()

@router.get("/", response_model=List[FornecedorOut])
def listar():
    return fornecedor_service.list_all()

@router.get("/{fid}", response_model=FornecedorOut)
def obter(fid: int):
    f = fornecedor_service.get(fid)
    if not f:
        raise HTTPException(status_code=404, detail="Fornecedor não encontrado")
    return f

@router.post("/", response_model=FornecedorOut, status_code=201)
def criar(payload: FornecedorIn):
    return fornecedor_service.create(payload.dict())

@router.put("/{fid}", response_model=FornecedorOut)
def atualizar(fid: int, payload: FornecedorIn):
    updated = fornecedor_service.update(fid, payload.dict(exclude_unset=True))
    if not updated:
        raise HTTPException(status_code=404, detail="Fornecedor não encontrado")
    return updated

@router.delete("/{fid}", status_code=204)
def remover(fid: int):
    ok = fornecedor_service.delete(fid)
    if not ok:
        raise HTTPException(status_code=409, detail="Registro não pode ser removido (FK ativa)")
    return None