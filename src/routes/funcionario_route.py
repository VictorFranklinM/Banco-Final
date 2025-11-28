from fastapi import APIRouter, HTTPException
from typing import List
from models.funcionario import FuncionarioIn, FuncionarioOut
from services import funcionario_service

router = APIRouter()

@router.get("/", response_model=List[FuncionarioOut])
def listar():
    return funcionario_service.list_all()

@router.get("/{func_id}", response_model=FuncionarioOut)
def obter(func_id: int):
    f = funcionario_service.get(func_id)
    if not f:
        raise HTTPException(status_code=404, detail="Funcionário não encontrado")
    return f

@router.post("/", response_model=FuncionarioOut, status_code=201)
def criar(payload: FuncionarioIn):
    return funcionario_service.create(payload.dict())

@router.put("/{func_id}", response_model=FuncionarioOut)
def atualizar(func_id: int, payload: FuncionarioIn):
    updated = funcionario_service.update(func_id, payload.dict(exclude_unset=True))
    if not updated:
        raise HTTPException(status_code=404, detail="Funcionário não encontrado")
    return updated

@router.delete("/{func_id}", status_code=204)
def remover(func_id: int):
    ok = funcionario_service.delete(func_id)
    if not ok:
        raise HTTPException(status_code=409, detail="Registro não pode ser removido (FK ativa)")
    return None