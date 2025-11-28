from fastapi import APIRouter, HTTPException
from typing import List
from models.andamento_ordem_servico import AndamentoOrdemServicoIn, AndamentoOrdemServicoOut
from services import andamento_ordem_servico_service

router = APIRouter()

@router.get("/", response_model=List[AndamentoOrdemServicoOut])
def listar():
    return andamento_ordem_servico_service.list_all()

@router.get("/{andamento_id}", response_model=AndamentoOrdemServicoOut)
def obter(andamento_id: int):
    a = andamento_ordem_servico_service.get(andamento_id)
    if not a:
        raise HTTPException(status_code=404, detail="Andamento não encontrado")
    return a

@router.post("/", response_model=AndamentoOrdemServicoOut, status_code=201)
def criar(payload: AndamentoOrdemServicoIn):
    return andamento_ordem_servico_service.create(payload.dict())

@router.put("/{andamento_id}", response_model=AndamentoOrdemServicoOut)
def atualizar(andamento_id: int, payload: AndamentoOrdemServicoIn):
    updated = andamento_ordem_servico_service.update(andamento_id, payload.dict(exclude_unset=True))
    if not updated:
        raise HTTPException(status_code=404, detail="Andamento não encontrado")
    return updated

@router.delete("/{andamento_id}", status_code=204)
def remover(andamento_id: int):
    ok = andamento_ordem_servico_service.delete(andamento_id)
    if not ok:
        raise HTTPException(status_code=409, detail="Registro não pode ser removido (FK ativa)")
    return None